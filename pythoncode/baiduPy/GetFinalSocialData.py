#encoding:utf-8
import sys
import datetime
import random

# 获取coreUser所用到的social data， 即与其相连的所有link

def main():
	starttime = datetime.datetime.now() 
		
	print 'load data...'
	socialList=GetSocialData()	
	coreUserList=GetCoreUserID()
	GetSocialDataAndWriteToTxt(coreUserList,socialList,'final')
	
	print 'finished'	
	endtime = datetime.datetime.now()   
	print 'passed time is %d s' % (endtime - starttime).seconds  
	

	
def GetSocialDataAndWriteToTxt(coreUserList,socialList,mark):
	codePath=sys.path[0]
	s=codePath.split('\\')
	workPath=s[0]+'\\'+s[1]+'\\'+s[2]+'\\data\\baidu\\commondata\\'  #f:\project\somproject
	writer=open(workPath+mark+'Social.txt','w')
	userSet=set()
	linkCount=0
	lineStoreList=[]
	for line in socialList:
		data=line[:-1].split('\t')
		origUserID=data[0]
		targetUserID=data[1]
		if origUserID in coreUserList or targetUserID in coreUserList:
			lineStoreList.append(line)
			userSet.add(origUserID)
			userSet.add(targetUserID)
			linkCount+=1
			
	writer.writelines(lineStoreList)
	
	print 'user num is %d' % len(userSet)	
	print 'link num is %d' % linkCount
	writer.close()	
		
	
	
def GetCoreUserID():
	codePath=sys.path[0]
	s=codePath.split('\\')
	workPath=s[0]+'\\'+s[1]+'\\'+s[2]+'\\data\\baidu\\commondata\\'  #f:\project\somproject
	f=file(workPath+'coreUserID.txt','r')
	dataList=f.readlines()
	f.close()
	coreUserList=list()
	for line in dataList:
		uid=line[:-1]
		coreUserList.append(uid)
	return coreUserList		
		
	
def GetSocialData():
	codePath=sys.path[0]
	s=codePath.split('\\')
	workPath=s[0]+'\\'+s[1]+'\\'+s[2]+'\\data\\baidu\\'  #f:\project\somproject
	ff=file(workPath+'social_set.txt','r')
	socialList=ff.readlines()
	ff.close()
	return socialList	
	
	
if __name__=='__main__':
	main()


