---
title: 'Solving Advent of Code with Kreya | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/solving-advent-of-code-with-kreya/'
original_language: en
published: 2023-12-01
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6dbf98e8688c016d'
translated: false
---

> 原文：[Solving Advent of Code with Kreya | Kreya](https://kreya.app/blog/solving-advent-of-code-with-kreya/)　·　Kreya Blog

Today I was sitting at my computer desk and it was raining and cold outside. Nothing special, just a Friday. I was implementing some code for a project and had to run over 2,000 tests. I started the tests and had a moment to surf the internet. Opened [Hacker News](https://news.ycombinator.com/) and saw the link to [Advent of Code 2023](https://adventofcode.com/). Like almost every year, I opened the page, logged in and looked at the first puzzle. My interest and motivation to solve such a puzzle was quite high.

I wanted to jump in, but then, like every year before, it hit me:

- **Which language should I use?** It had to be something simple and quick. JavaScript. Okay, off we go!
- **How do I download the text file?** Downloading and copying the file is a pain and my motivation is dropping.
- **How do I read the text file?** Creating some I/O functions is also a pain, and of course I can copy/paste it from the internet, but I don't know, my motivation was gone.

Then I had an idea, is it possible to solve these puzzles with Kreya? I opened Kreya and tried to get it working. After a little research I set up an REST operation with authentication and was ready to get the input file of the puzzle.

To authenticate you need to login and copy your session cookie at [https://adventofcode.com](https://adventofcode.com), which can be found in your browser's storage. The cookie is called "session" and can be sent in Kreya with the header "Cookie: session=value". The endpoint `https://adventofcode.com` must be defined in the Settings tab. You should now have your own puzzle input file in the response view.

In the Scripting tab I was able to start directly with the input file as string and didn't need to download any file or read it in any way. Here is the boilerplate without the solution:

```js
kreya.rest.onCallCompleted(call => {  const input = call.response.rawContentText;  let result = 0;  // ... your solution belongs here :)  kreya.trace('Result:' + result);});
```

To see the result, you can log a message in the Trace tab with the command `kreya.trace()`.

After a short time I had the first solution to the puzzle and was excited to solve more.

**Spoiler ahead**: The script contains my solution to the first puzzle.

```js
kreya.rest.onCallCompleted(call => {    const regex = /(\d)/g;    let result = 0;    const lines = call.response.rawContentText.split('\n');    lines.forEach(line => {        const matches = [...line.matchAll(regex)];        if (matches == undefined || matches[0] == undefined) {            return;        }            result += +(matches[0][0] + matches[matches.length - 1][0]);    });    kreya.trace('Result:' + result);});
```

Now it's evening and the rain outside has turned to snow. I'm writing this blog post because I think there are more people like me who are interested in these puzzles but struggle to create an environment that makes solving them fun. For me it's Kreya, because I can use the input string directly from the puzzle and write some JavaScript. If you want to try this, you can download Kreya and create a [subscription](https://kreya.app/pricing/) as the [scripting feature](https://kreya.app/docs/scripting-and-tests/) is a Pro feature. But it's free for the first 10 days!

Happy coding and see you ❄️ 🎅
