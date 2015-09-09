from bs4 import BeautifulSoup
from urllib2 import urlopen

soup=BeautifulSoup(open('html_doc.txt').read(),'lxml')
table_class=soup.find('table',{"class":"chart full-width"})
print "Top 20 Films out of ",soup.h1.text," On IMDB" 
#print table_class
ans=[tuple()]
for link in table_class.find_all('tr')[1:21]:
    #tds=row('td')
    #print link
    R=link.find('td',{"class":"titleColumn"})
    ans=R.text
    print "Rank: ",ans.split()[0],
    print "Title of Movie: ",R.find('a').text, # Title of movie
    print "Year of Release:",R.find('span').text,
    Rating=link.find('td',{"class":"ratingColumn imdbRating"})
    print "Rating:",Rating.text,
    print 
    
