#!/usr/bin/python3
import random
import http.client 
import socket

def get_vocabulary():
    # generate a vocabulary
    words_nb=5000
    words=[]
    max_word_len=12
    for i in range(0,words_nb):
        words.append('')
        # first choose a randon length
        wlen=random.randrange(1,max_word_len) # 
        for j in range(0,wlen):
            k=12
            word=words.pop()
            word=word+chr(random.randrange(97,123)) # ASCII lowecase characters
            words.append(word)
    return words


def generate_doc(words):
    doc=[]
    # generate one document
    words_in_document=10000
    for i in range(0,words_in_document):
        word=words[random.randrange(0,len(words))]
        doc.append(word)
    res=' '.join(doc)
    return res


words=get_vocabulary()


print(words)
print(generate_doc(words))

for i in range(0,1):
    pass

# curl -X POST --user admin:admin -F filedata=@test.txt -F uploaddirectory=/folder1 -F "destination=workspace://SpacesStore/17192e81-1e44-4371-8e5a-8a8e7a3481aa" http://localhost:8080/alfresco/service/api/upload

# curl -X POST --user admin:admin -F filedata=@test.txt -F uploaddirectory=/folder1 -F "destination=workspace://SpacesStore/17192e81-1e44-4371-8e5a-8a8e7a3481aa" -H "Expect:" http://localhost:8080/alfresco/service/api/upload
 
# workspace://SpacesStore/0b423f45-4e2d-44be-bb93-ba3b6d49214d
# workspace://SpacesStore/17192e81-1e44-4371-8e5a-8a8e7a3481aa
#!/usr/bin/env python3
"""
boundary="----------------------------4a227aed0702"
headers = {"Content-type": "multipart/form-data; boundary=--"+boundary, "Authorization":"Basic YWRtaW46YWRtaW4=","Accept": "*/*","User-Agent":"curl/7.27.0"}

fields=[("uploaddirectory","/folder1"),("destination","workspace://SpacesStore/17192e81-1e44-4371-8e5a-8a8e7a3481aa")]
L = []
L.append('--' + boundary)
L.append('Content-Disposition: form-data; name="filedata"; filename="test.txt"')
L.append('Content-Type: text/plain')
L.append('')
L.append('somecontent\n')
for (key, value) in fields:
    L.append('--' + boundary)
    L.append('Content-Disposition: form-data; name="%s"' % key)
    L.append('')
    L.append(value)

L.append('--' + boundary + '--')
L.append('')
body = '\r\n'.join(L)
print(body)

h = http.client.HTTPConnection('localhost:8080')
h.request('POST', '/alfresco/service/api/upload', body=body,headers=headers)
print(h.getresponse().read())
"""
s = socket.socket() 
a=[]
a.append(b'POST /alfresco/service/api/upload HTTP/1.1')
a.append(b'Authorization: Basic YWRtaW46YWRtaW4=')
a.append(b'User-Agent: curl/7.27.0')
a.append(b'Accept-Encoding: identity')
a.append(b'Host: localhost:8080')
a.append(b'Accept: */*')
a.append(b'Content-Length: 474')
a.append(b'Content-Type: multipart/form-data; boundary=----------------------------4a227aed0702')

a.append(b'')
a.append(b'------------------------------4a227aed0702')
a.append(b'Content-Disposition: form-data; name="filedata"; filename="test.txt"')
a.append(b'Content-Type: text/plain')
a.append(b'')
a.append(b'somecontent')
a.append(b'')
a.append(b'------------------------------4a227aed0702')
a.append(b'Content-Disposition: form-data; name="uploaddirectory"')
a.append(b'')
a.append(b'/folder1')
a.append(b'------------------------------4a227aed0702')
a.append(b'Content-Disposition: form-data; name="destination"')
a.append(b'')
a.append(b'workspace://SpacesStore/17192e81-1e44-4371-8e5a-8a8e7a3481aa')
a.append(b'------------------------------4a227aed0702--')
a.append(b'')


s.connect(('localhost', 8080))
# s.send(b"GET / HTTP/1.0\n\n")
s.send(b'\r\n'.join(a))
print(s.recv(1024))
s.close
