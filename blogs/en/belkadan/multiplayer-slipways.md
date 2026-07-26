---
title: Multiplayer Slipways
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/08/Multiplayer-Slipways/'
original_language: en
published: 2023-08-12
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:7e337af85ab84a61'
translated: false
---

> 原文：[Multiplayer Slipways](https://belkadan.com/blog/2023/08/Multiplayer-Slipways/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Re: Twitter](https://belkadan.com/blog/2022/12/Re-Twitter/)

[Trunic](https://belkadan.com/blog/2024/07/Trunic/) »

« [JavaScript Tetris](https://belkadan.com/blog/2009/03/JavaScript-Tetris/?tag=games)

[Trunic](https://belkadan.com/blog/2024/07/Trunic/?tag=games) »

## [Multiplayer Slipways](#)

I’ve been enjoying [Slipways](https://slipways.net), a space exploration/economy game with the tagline “Build vast space empires. Still be done in time for lunch.” Roughly speaking, Slipways is a mini version of [Stellaris](https://www.paradoxinteractive.com/games/stellaris/) the way [Polytopia](https://polytopia.io) (also recommended) is a mini version of [Civilization](https://civilization.com).

But Polytopia is a multiplayer game, and I like casual multiplayer games like that. And Stellaris and Civilization support multiplayer too. And even though Slipways isn’t a combat game, or really a competitive game in any way[1](#fn:OTC), I think you could make a good _cooperative_ multiplayer game out of it: two empires trying to achieve the highest possible score together.more

![](https://belkadan.com/blog/2023/08/Multiplayer-Slipways/screenshot.jpg)

The catch is that Slipways single-player allows you to undo any action that doesn’t give you (significant) new information, and this is a core part of what makes it a low-stress game. I’d want to preserve that in multiplayer Slipways, but not force the two players to be in sync all of the time. Fortunately, there’s another feature that helps balance this out: most passive effects, such as income, upkeep, and research, only happen on year boundaries. As long as we establish that interactions between the two players can only result in _positive_ end-of-year effects, we can allow one player to race ahead of the other even across year boundaries:

- If the player who’s ahead Undoes an action, that has no effect on the player who’s behind. (Unless it’s a multi-month action, and undoing it would swap who’s ahead. We’re going to ignore that case but you can work out reasonable rules for it.)
- If the player who’s behind Undoes an action that does not cross a year boundary, that has no effect on the player who’s ahead.
- If the player who’s behind Undoes an action that _does_ cross a year boundary, they have to get confirmation from the other player. The player who’s ahead gets three options: “Accept”, “Accept and roll back to last checkpoint”, and “Reject”. Plain “Accept” may not be available if the player who’s ahead depended on something that happened on that year boundary. In the case where the player who’s ahead can’t roll back far enough due to newly-discovered information, “Reject” will be the only available option. (Hey, we tried very hard to prevent this scenario, but sometimes it’s gonna happen!)

In practice, I think these rules will encourage players not to get too far apart in time.

After hammering all that out, the rest is just details:

- The player who’s behind should see “claims” from the player who’s ahead for all planets, slipways, and structures, to prevent overlap. The UI could even include dates of completion.
- Connections between empires are allowed, but the trade income is split. ¾ for the sender and ¼ for the receiver makes sense to me, but someone would have to make sure that ¼ is enough to counterbalance upkeep costs inflicted on another player (to maintain the rule about positive end-of-year effects). Cross-empire connections can still count as “successful neighbors”.
- Money is separate for each empire, but either player can voluntarily give money to the other in a particular month. If one player goes bankrupt at the end of the year, the other can give them money as long as they are no more than a year ahead. This is the one place you can get money from the future, because otherwise the game ends for both players.
- Technology can be played in two modes:

    1. **Shared**: Both users share a single science budget and tech tree. Research has to be confirmed by both users, as does Undoing research. Research from a player who’s ahead does not take effect until that month, but preallocates science resources from the perspective of the player who’s behind.
    2. **Separate**: Each user has their own science budget and tech tree. However, routes that generate science are assigned based on the supplier of people (or bots, in cases where bots are doing the research rather than being researched). Supplied resources generate bonuses for both players. _Example: a research station with two researchers from Alex and one from Sam, plus two total resource units being studied, generates 4 science for Alex and 3 for Sam._

  Both of these modes result in science being more accessible than in a single-player game, so costs might need to be raised accordingly.
- I don’t actually know if shared vision makes sense or not. My gut says that even for empires with a long common border it wouldn’t make that much of a difference.

---

Of course, all this is easier said than done. I’d also like a mobile tablet port (they’re currently working on a Switch release), and maybe a pony. I’m not sure a two-player co-op mode is _really_ the best next thing to focus on. But it would be neat. And in case it’s not clear from how much time I’ve spent thinking about this, I do recommend Slipways as a single-player game. Thanks to friends C and Y for telling me about it!

1. For a competitive space game that isn’t a combat game, there’s [Offworld Trading Company](https://www.offworldgame.com). I never got very good at it, but it was definitely an interesting model! [↩︎](#fnref:OTC)

This entry was posted on [August](https://belkadan.com/blog/2023/08) 12, [2023](https://belkadan.com/blog/2023) and is filed under [Personal](https://belkadan.com/blog/personal). Tags: [Games](https://belkadan.com/blog/tags/games)
