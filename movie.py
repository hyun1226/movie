import requests
from bs4 import BeautifulSoup

basic_URL = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=182387&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='
for i in range(1,50):
    URL = basic_URL + str(i)

    html = requests.get(URL).text

    soup = BeautifulSoup(html, 'html.parser')
    score_result= soup.find("div",{"class":"score_result"})

    all_lis = score_result.find_all('li')
    for li in all_lis:
        single_comment = li.find("span",{"class":"_unfold_ment"})
        try:
            single_comment = single_comment.find("a")
            single_comment = single_comment['data-src']
        except:

            single_comment = li.find('div',{'class':'score_reple'}).find('p')
            single_comment = single_comment.find_all('span')
            if len(single_comment)>1:
                single_comment = single_comment[1].text.strip()
            else:
                single_comment = single_comment[0].text.strip()

        print(single_comment)

