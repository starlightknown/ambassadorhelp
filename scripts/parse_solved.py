import re,html,json,glob
idx=dict(l.split(' ',1) for l in open('forum/topics/index.txt').read().split('\n') if l)
out=[]
for i,url in idx.items():
    s=open(f'forum/topics/t{i}.html',encoding='utf8').read()
    m=s.find('best-answer-banner')
    if m<0: continue
    seg=s[m:m+8000]
    g=lambda r,t=seg:(lambda x:html.unescape(x.group(1)).strip() if x else None)(re.search(r,t,re.S))
    body=g(r'post__content[^"]*">(.*?)</div>')
    body=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',body or ''))).strip()
    # first post (question)
    q=s[s.find('qa-topic-first-post') if 'qa-topic-first-post' in s else 0:]
    title=g(r'<h1[^>]*>(.*?)</h1>',s)
    out.append(dict(url=url.strip(),title=re.sub('<[^>]+>','',title or ''),answerer=g(r'aria-label="Best answer by ([^"]+)"'),
      rank=g(r'rank-title">([^<]+)<'),adate=g(r'<time dateTime="([^"]+)"'),
      qdate=g(r'<time dateTime="([^"]+)"',s[s.find('</h1>'):]),
      asker=g(r'qa-username[^>]*>([^<]+)<',s[s.find('</h1>'):]),
      askrank=g(r'rank-title">([^<]+)<',s[s.find('</h1>'):]),
      excerpt=body[:280]))
json.dump(out,open('solved.json','w'),ensure_ascii=False,indent=1)
import collections
print(len(out)); print(collections.Counter(o['rank'] for o in out).most_common())
print(collections.Counter(o['answerer'] for o in out).most_common(20))
print(min(o['qdate'] or 'z' for o in out), max(o['qdate'] or '' for o in out))
print(sum(o['answerer']==o['asker'] for o in out),'self-answered')
