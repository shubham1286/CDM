from bs4 import BeautifulSoup

import urllib2

from urllib2 import urlopen, URLError

import re

import csv

import unicodedata

import codecs

import os

import sys

vv=0

tempo=0

total=0

flag=1
class app():
    
   
   def cdm1(self,text,filename):

       
        
        req=urllib2.Request(str(text))

        try: ss=urllib2.urlopen(str(text))

        except URLError as e:
            return (0,0)
             
        url=str(text).split("/");
       
        xx=ss.read()

        global total

        total=len(xx)
        
        soup = BeautifulSoup(xx)

        
        ss=url[3]+".cpp"
        

        if "codechef" in url[2]:
           
           global tempo

           self.temp=0

           global vv

           self.hh=0

           self.kkk=1

           prefix="http://www.codechef.com"


           for link in soup.findAll("a"):
              oo=link.get("href")

              if "status" in oo and self.kkk==1:

                 rr=str(oo).split("/")

                 self.kkk=0
                
                 out=open(filename,"w")
                 out.write("// it's a scrapped code by CDM!!!!\n\n")

              if "viewplaintext" in oo:

                prefix+=oo

                pp=urllib2.urlopen(prefix).read()

                dd=BeautifulSoup(pp)

                for hh in dd.findAll("pre"):

                   kk=hh.get_text().encode('UTF-8')

                   self.temp=self.temp+len(kk)

                   tempo=self.temp

           for link in soup.findAll("a"):

              oo=link.get("href")

              if "viewplaintext" in oo:

                prefix+=oo

                pp=urllib2.urlopen(prefix).read()

                dd=BeautifulSoup(pp)

                for hh in dd.findAll("pre"):

                   kk=hh.get_text().encode('UTF-8')

                   self.hh=self.hh+len(kk)

                   vv=self.hh

                   out.write(kk)

                   out.write("\n\n")

           return (vv,tempo)
         
        else:
          output = open(filename,'w')

          output.write("// it's a scrapped code by CDM!!!!\n\n")

          global tempo

          self.temp=0

          global vv

          self.hh=0


          for link in soup.findAll(re.compile("^p")):

               line=link.get_text().encode('UTF-8')

               
               self.temp=self.temp+len(line)

               tempo=self.temp
               
               if 'comments' in line:
                 break
               if 'GeeksQuiz'in line:
                 continue

               if 'Login' in line:
                 continue

               
        

          self.flag=1

          for link in soup.findAll(re.compile("^p")):
               
               line=link.get_text().encode('UTF-8')

               if(self.flag==0):
                   break
                
               self.hh=self.hh+len(line)
               
               vv=self.hh

               s_plit=str(line).split("\ ; .")

               for no in s_plit:

                  if 'comments' in no:
                     self.flag=0
                     break;

                  if 'GeeksQuiz'in no:
                     continue

                  if 'Login' in no:
                     continue

                  output.write(no)

                  output.write("\n\n")

            
          return (vv,tempo) 
        

        
       
