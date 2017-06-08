#!/usr/bin/python3
import random
import http.client 
import codecs

WORDS_PER_DOC=10000 # see lucene.indexer.maxFieldLength=10000
WORDS_IN_VOCABULARY=300000 # number of possible tokens in the vocubalary (used to generate a simple vocab) 5000, 20000, 100
MIN_WORD_LEN=50 # 1
MAX_WORD_LEN=100 # 12
DOC_NB=10000 # 1000
COMPANY_HOME="workspace://SpacesStore/aaf01622-4393-4b82-8816-a5dab028bf77" #  # used by upload REST API

def get_vocabulary():
    # generate a vocabulary, may contain duplicate
    words=[]
    for i in range(0,WORDS_IN_VOCABULARY):
        words.append('')
        # first choose a randon length
        wlen=random.randrange(MIN_WORD_LEN,MAX_WORD_LEN) # 
        for j in range(0,wlen):
            word=words.pop()
            word=word+chr(random.randrange(97,123)) # ASCII lowecase characters
            words.append(word)
    return words

def get_vocabulary2():
    words=[]
    for i in range(97,123):
        word=chr(i)
        words.append(word)
        for j in range(97,123):
            word=chr(i)+chr(j)
            words.append(word)
            for k in range(97,123):
                word=chr(i)+chr(j)+chr(k)
                words.append(word)
                for l in range(97,123):
                    word=chr(i)+chr(j)+chr(k)+chr(l)
                    words.append(word)
    print(words)
    print(len(words))
    return words

def get_vocabulary3():
    # 21341
    words=[]
    planes=[
        ('\u0030','\u0039'), # digits
        ('\u0061','\u007A'), # letters
        ('\u03AC','\u03C9'), # greek
        ('\u0430','\u044E'), # cyrillic
        ('\u05D0','\u05EA'), # hebrew
        ('\u0622','\u06D3'), # arabic
        ('\u0E01','\u0E2F'), # thai
        # 4E00-62FF, 6300-77FF, 7800-8CFF, 8D00-9FFF. CJK
        ('\u4E00','\u62FF'), # 
        ('\u6300','\u77FF'), # 
        ('\u7800','\u8CFF'), # 
        ('\u8D00','\u9FFF'), # 
        ]
    for (afrom, ato) in planes:
        for i in range(ord(afrom),ord(ato)+1):
            print('%X'%i, chr(i))
            words.append(chr(i))
    print(words)
    print(len(words))
    return words



def generate_doc(words):
    doc=[]
    # generate one document
    words_in_document=WORDS_PER_DOC # see lucene.indexer.maxFieldLength=10000
    for i in range(0,words_in_document):
        word=words[random.randrange(0,len(words))]
        doc.append(word)
    res=' '.join(doc)
    return res



def post_one_file(filedata,filename):
    boundary="------------------------------4a227aed0702"
    headers = {"Content-type": "multipart/form-data; boundary="+boundary, "Authorization":"Basic YWRtaW46YWRtaW4=","Accept": "*/*","User-Agent":"curl/7.27.0"}
    fields=[("uploaddirectory","/folder1"),("destination",COMPANY_HOME)]
    L = []
    L.append('--' + boundary)
    L.append('Content-Disposition: form-data; name="filedata"; filename="%s"'% filename)
    L.append('Content-Type: text/plain')
    L.append('')
    L.append(filedata)
    for (key, value) in fields:
        L.append('--' + boundary)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    L.append('--' + boundary + '--')
    L.append('')
    body = '\r\n'.join(L)
    # print(body)
    h = http.client.HTTPConnection('localhost:8080')
    h.request('POST', '/alfresco/service/api/upload', body=body.encode('utf-8'),headers=headers)
    print(h.getresponse().read())


if __name__ == "__main__":
    words=get_vocabulary3()
    
    
    # print(words)
    # quit()

    for i in range(0,DOC_NB):
        filedata=generate_doc(words)
        filename="file_%06i.txt" %i
        post_one_file(filedata,filename)

# curl -X POST --user admin:admin -F filedata=@test.txt -F uploaddirectory=/folder1 -F "destination=workspace://SpacesStore/17192e81-1e44-4371-8e5a-8a8e7a3481aa" http://localhost:8080/alfresco/service/api/upload

# curl -X POST --user admin:admin -F filedata=@test.txt -F uploaddirectory=/folder1 -F "destination=workspace://SpacesStore/17192e81-1e44-4371-8e5a-8a8e7a3481aa" -H "Expect:" http://localhost:8080/alfresco/service/api/upload
 
# workspace://SpacesStore/0b423f45-4e2d-44be-bb93-ba3b6d49214d
# workspace://SpacesStore/17192e81-1e44-4371-8e5a-8a8e7a3481aa
