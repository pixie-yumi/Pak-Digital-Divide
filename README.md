# Pakistan's Digital Gender Divide

A small data analysis project where I wanted to work with something real and current, so I dug into Pakistan's own government survey data on internet and mobile phone access.

## What I found

The short version: men own way more phones than women in Pakistan (69% vs 31% nationally), and the gap is worst in rural areas. But once women actually get access to a phone or the internet, by any means, they use it just as much as men do, and in cities, slightly more.

That told me something I wasn't expecting going in: the problem isn't that women don't want to use the internet or don't know how. It's that they don't own the device in the first place. So if you're trying to fix this, the answer probably isn't another digital literacy program, it's getting women their own phones.

There's also a straightforward urban vs rural infrastructure gap on top of this (82% vs 61% household internet access), and separately, 76% of people nationally have no financial account at all, which matters because phone ownership is usually the first step toward mobile banking.

## Data source

Pakistan Bureau of Statistics, HIES 2024-25 Social Report (with 2018-19 figures pulled from the previous PSLM round for comparison). I typed the numbers in by hand from the actual PDF tables since the report doesn't come as a clean downloadable CSV, which honestly took longer than I expected but I wanted to work from something official rather than a random secondhand dataset.

## How it's built

- Data cleaned and structured manually into a CSV (indicator, group, region, 2024-25 value, 2018-19 value)
- Queried in SQLite to calculate gender and urban/rural gaps
- Visualized in a Streamlit dashboard

Live dashboard: https://pak-digital-divide-24-25.streamlit.app

## Why this scope

I kept this to four indicators (mobile ownership, internet use, household access, financial inclusion) instead of trying to cover everything in the survey. The report has way more in it, education, health, housing, but I wanted something focused enough to actually finish properly rather than a shallow pass over everything.

Province-level breakdown is the obvious next step if I extend this later.
