# Pakistan's Digital Gender Divide

69% of men in Pakistan own a mobile phone. Only 31% of women do. That's the number that got me started on this.

I wanted to dig into something real and current, so I pulled apart Pakistan's own government survey data on who actually has internet and mobile access, and who doesn't.

## What I found

Here's the part that actually surprised me: the ownership gap is huge, but once women get access to a phone or the internet by any means, they use it just as much as men, and in cities, slightly more.

That flips the whole assumption. It's not that women don't want to use the internet, or don't know how. It's that they don't own the device in the first place. So if you were designing a program to close this gap, the answer isn't another digital literacy workshop, it's putting phones in women's hands.

Rural women get hit twice: the widest ownership gap and the weakest internet infrastructure. And zooming out further, 76% of people nationally have no financial account at all, which matters here because phone ownership is usually step one toward mobile banking.

## Data source

Pakistan Bureau of Statistics, HIES 2024-25 Social Report, cross-checked against the 2018-19 PSLM round to see what's actually changed. The numbers don't come as a clean CSV, so I typed them in by hand straight from the PDF tables. Slower than downloading a dataset, but I wanted this built on something official.

## How it's built

- Data structured manually into a CSV (indicator, group, region, 2024-25 value, 2018-19 value)
- Queried in SQLite, using joins to calculate gender and urban/rural gaps
- Visualized in a Streamlit dashboard

Live dashboard: https://pak-digital-divide-24-25.streamlit.app

## Why this scope

The full report covers education, health, housing, food security, way more than digital access alone. I picked four indicators (mobile ownership, internet use, household access, financial inclusion) that build on each other: who owns a device, who actually uses it, whose home has a connection, and what that unlocks financially.

Province-level breakdown is the natural next step if I take this further.
