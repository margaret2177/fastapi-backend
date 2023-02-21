from requests_html import HTMLSession
# from requests_html import AsyncHTMLSession





class Scraper:
	s = HTMLSession()

	def homeThumbnail(self,page,filter):
		print('page in scrap',page)
		if filter == 'RAS':
			url = f'https://asianembed.io/?page={page}'
		else:
			url = f'https://asianembed.io/{filter}?page={page}'
		print('url',url)
		r = self.s.get(url)
		try:
			ul = r.html.find('.listing',first=True)
			# print(ul.find('.video-block'))
			thumbData=[]
			for u in ul.find('.video-block'):
				print(u)
			for i in ul.find('.video-block'):
				data={}
				data['link']=i.find('a',first=True).attrs['href'].split('videos')[1].replace('/','')
				data['img'] = i.find('.picture',first=True).find('img',first=True).attrs['src']
				data['name'] = i.find('.name',first=True).text.strip()
				data['meta'] = i.find('.meta',first=True).text.strip()
				thumbData.append(data)

			# print(thumbData)
			pagination = r.html.find('.pagination',first=True)
			hasMore = True if pagination.find('.next') else False
			# print({'videos':thumbData,'page':page, 'hasMore':hasMore})
			return {'videos':thumbData,'page':page, 'hasMore':hasMore}
		except Exception as e:
			raise e


	def itemDetails(self,item):
		
		r = self.s.get(f'https://asianembed.io/videos/{item}')
		try:
			videoInfo = r.html.find('.video-info-left',first=True)
			title = videoInfo.find('h1',first=True).text.strip()
			iframe = videoInfo.find('iframe',first=True).attrs['src']
			details = videoInfo.find('.video-details',first=True).text.strip()

			lists = videoInfo.find('.lists',first=True)

			thumbData=[]
			
			for i in lists.find('.video-block'):
				data={}
				data['link']=i.find('a',first=True).attrs['href'].split('videos')[1].replace('/','')
				data['img'] = i.find('.picture',first=True).find('img',first=True).attrs['src']
				data['name'] = i.find('.name',first=True).text.strip()
				data['meta'] = i.find('.meta',first=True).text.strip()
				thumbData.append(data)
			details={
				'title':title,
				'src':iframe,
				'details':details,
				'episodes':thumbData
				}
			# print(details)
			return details
		except Exception as e:
			pass
		


	def searchResult(self,term,page):

		r =  self.s.get(f'https://asianembed.io/search.html?keyword={term}&page={page}')
		ul =r.html.find('.listing',first=True)

		resultInfo=[]
		for i in ul.find('.video-block'):
			data={}
			data['link']=i.find('a',first=True).attrs['href'].split('videos')[1].replace('/','')
			data['img'] = i.find('.picture',first=True).find('img',first=True).attrs['src']
			data['name'] = i.find('.name',first=True).text.strip()
			# data['meta'] = i.find('.meta',first=True).text.strip()
			resultInfo.append(data)
		pagination = r.html.find('.pagination',first=True)
		hasMore = True if pagination.find('.next') else False
		
		print({'results':resultInfo,'page':page,'hasMore':hasMore})
		return {'results':resultInfo,'page':page,'hasMore':hasMore}






# s = Scraper()

# s.homeThumbnail()
# s.itemDetails('avataro-sentai-donbrothers-2022-episode-24')



# iframes = []	
# for link in links:
# 	r2 = s.get('https://asianembed.io/videos/avataro-sentai-donbrothers-2022-episode-24')
# 	f = r2.html.find('.play-video',first=True)
# 	iframes.append(f.find('iframe',first=True).attrs['src'])

# print(iframes)



