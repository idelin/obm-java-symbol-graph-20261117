import json
def receive(stream):
    headers={}
    while True:
        line=stream.readline()
        if not line:return None
        if line in (b'\r\n',b'\n'):break
        k,v=line.decode('ascii').split(':',1);headers[k.lower()]=v.strip()
    n=int(headers['content-length']);body=b''
    while len(body)<n:
        part=stream.read(n-len(body))
        if not part:raise EOFError()
        body+=part
    return json.loads(body)
def send(stream,obj):
    body=json.dumps(obj,separators=(',',':'),ensure_ascii=False).encode();stream.write(('Content-Length: '+str(len(body))+'\r\n\r\n').encode()+body);stream.flush()
