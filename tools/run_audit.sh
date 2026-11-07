#!/bin/bash
# Responsive audit: every page at every width. Prints only pages with problems.
# usage: tools/run_audit.sh [quick]   (needs: python3 -m http.server 3011 running in the project root)
B=~/.claude/skills/gstack/browse/dist/browse
cd "$(dirname "$0")/.."
PAGES="index.html about.html guides.html collaborate.html privacy.html terms.html refund.html cookies.html hi/index.html hi/about.html hi/guides.html hi/collaborate.html hi/privacy.html hi/terms.html hi/refund.html hi/cookies.html"
VPS="320x700 360x740 375x812 390x844 414x896 480x854 600x900 768x1024 820x1180 1024x768 1280x800 1440x900 1920x1080"
[ "$1" = "quick" ] && VPS="320x700 375x812 768x1024 1440x900"
JS="$(cat tools/audit.js)"
for vp in $VPS; do
  $B viewport $vp >/dev/null 2>&1
  for pg in $PAGES; do
    $B goto http://localhost:3011/$pg >/dev/null 2>&1; sleep 1.2
    r=$($B js "$JS" 2>&1 | tail -1)
    echo "$r" | python3 -c "
import sys,json
try: d=json.loads(sys.stdin.read())
except Exception as e: print('$vp $pg PARSE_ERROR'); sys.exit()
bad={k:v for k,v in d.items() if k in('over','clip','tap','tiny','img') and v}
if d['sw']>d['w']+1: bad['scroll']=d['sw']
if bad: print('$vp $pg',json.dumps(bad,ensure_ascii=False))
"
  done
done
echo AUDIT_DONE
