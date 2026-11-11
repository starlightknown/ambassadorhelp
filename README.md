# Ambassador Assist

A concept prototype that extends the Figma Forum Ambassadors program. It's an independent proposal and isn't affiliated with Figma.

The [Ambassador program](https://forum.figma.com/forum-news-and-guidelines-25/announcing-figma-forum-ambassadors-59328) launched on 26 Oct 2026 with six founding members. Ambassador Assist would help them spend their time on open questions they're well placed to answer, then turn their best answers into reusable guides.

**Live page:** `index.html`, served with GitHub Pages.

## What's on the page

The page is what an Ambassador would see each week:

- **Picked for you this week.** Up to five open how-to questions from Ask the Community, filtered to the areas the Ambassador chooses. Questions with no reply come first, then the most viewed. Billing, account, plugin-review and bug questions are left out because they belong with Figma Support.
- **Leaderboard.** Points from accepted answers: +10 for a solution, +5 when the asker is a New Member, +5 for solving within 24 hours. Replies that don't solve anything earn nothing. It toggles between "Since launch" and "12 weeks".
- **What's happening.** Recent solutions with the points earned, questions that have waited longest, and program news.

## How "Help others" differs

The forum's "Help others" tab lists every topic without an accepted answer. Everyone sees the same list, sorted by recent activity, and most of it is bug reports and billing. Ambassador Assist uses the same pool but:

- filters it to questions a peer can answer,
- matches questions to each Ambassador's topic areas,
- puts unanswered questions first,
- sends a short weekly digest instead of expecting people to browse,
- turns verified answers into credited guides.

## Data and method

All data comes from public forum pages a logged-out visitor can see. It is a snapshot from **11 Nov 2026**, and the page itself does not fetch anything live.

1. **Fetch.** `scripts/fetch.sh` downloads the "Help others" listing (17 pages) and the 12 most recent pages of Ask the Community. The 120 solved threads among those were then downloaded one by one.
2. **Parse.** `scripts/parse_listing.py` reads each topic card: title, category, asker rank, replies and views. `scripts/parse_solved.py` reads the "Best answer by" block and the answerer's rank on each solved thread. These are one-off research scripts and expect the snapshot folder layout they were written against.
3. **Classify.**
   - Staff means the forum's Figmate rank, which also covers members titled Community Support.
   - Community means everyone else, including Ambassadors.
   - An asker who marked their own reply as the answer counts as self-solved.
4. **Route.** The 65 open Ask the Community questions were given a topic area and a route **by hand**. In production, Gainsight's topic tagging or a language model would do this, with fixed rules that keep billing, account and bug questions with Support.

### Files

- `data/accepted-answers.json`: the 120 accepted answers with answerer, rank and dates.
- `data/peer-answers.json`: weekly staff/community/self counts and the 10 community answers.
- `data/routed-questions.json`: the 46 open questions suited to Ambassadors, with their topic areas.

### Limits

- This is a sample of one category, not the forum's full history.
- Ranks are the ones shown today, so Ambassadors' answers from before the launch count as community answers.
- The topic tags and routes are manual.
- The change after launch is based on 21 accepted answers, so treat it as an early signal.

## Deploy

GitHub → **Settings → Pages → Build and deployment**: set the source to *Deploy from a branch*, choose `main` and `/ (root)`, then save. The site appears at `https://starlightknown.github.io/ambassadorhelp/`.
