import sys
from documents import Documents
from framing import receive,send
state=Documents()
while True:
    q=receive(sys.stdin.buffer)
    if q is None:break
    method=q.get('method');p=q.get('params',{});result=None
    if method=='textDocument/didOpen':state.open(p['textDocument'])
    elif method=='textDocument/didClose':state.close(p['textDocument']['uri'])
    elif method=='initialize':result={'capabilities':{'positionEncoding':'utf-16','textDocumentSync':1}}
    elif method=='exit':break
    if 'id' in q:send(sys.stdout.buffer,{'jsonrpc':'2.0','id':q['id'],'result':result})
