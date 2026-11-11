import sys,re,html,json
out=[]
for f in sys.argv[1:]:
    s=open(f,encoding='utf8').read()
    parts=s.split('class="topic-view_header"')[1:]
    for p in parts:
        g=lambda r:(lambda m:html.unescape(m.group(1)).strip() if m else None)(re.search(r,p,re.S))
        out.append(dict(
          user=g(r'qa-username[^>]*>([^<]+)<'),
          utitle=g(r'user-title text--meta">([^<]*)<'),
          cat=g(r'category-link">([^<]+)<'),
          title=g(r'title-link">([^<]+)<'),
          url=g(r'href="([^"]+)" class="qa-topic-title'),
          views=g(r'thread-meta-item__text">(\d+)</span></span></span>'),
          replies=g(r'aria-label="(\d+) repl'),
          likes=g(r'js-vote-count qa-topic-meta-likes-content">\s*(\d+)'),
          date=g(r'<time[^>]*datetime="([^"]+)"') or g(r'(\d+ (?:minutes?|hours?|days?|months?) ago)'),
        ))
print(json.dumps(out,ensure_ascii=False))
