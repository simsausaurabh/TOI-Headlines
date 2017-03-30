from bs4 import BeautifulSoup
import requests

def main():

	# Times Of India url
	url = 'http://timesofindia.indiatimes.com/home/headlines'

	# Response for the request of the url
	response = requests.get(url)

	html = response.content

	# Using BeautifulSoup to extract data(Headlines) from the html page
	soup = BeautifulSoup(html, "lxml")

	# Headlines present in: <span class="w_tle"><a href="/auto/miscellaneous/example/articleshow/57906990.cms" title="example" pg="#2">example</a></span>
	span_tags = soup.find_all('span', attrs={"class": "w_tle"})


	for span in span_tags:
		a_tag = span.find('a')
		print("--> "+a_tag.contents[0])

if __name__ == '__main__':
	main()
