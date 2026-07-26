---
title: Trunic
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2024/07/Trunic/'
original_language: en
published: 2024-07-17
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ad2f1187f70ba1bd'
translated: false
---

> 原文：[Trunic](https://belkadan.com/blog/2024/07/Trunic/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Multiplayer Slipways](https://belkadan.com/blog/2023/08/Multiplayer-Slipways/)

[“Pretty Good, Pretty Good”](https://belkadan.com/blog/2025/01/Pretty-Good-Pretty-Good/) »

« [Multiplayer Slipways](https://belkadan.com/blog/2023/08/Multiplayer-Slipways/?tag=games)

[“Pretty Good, Pretty Good”](https://belkadan.com/blog/2025/01/Pretty-Good-Pretty-Good/?tag=games) »

## [Trunic](#)

Last weekend I spent several hours on Tunic’s “offline” puzzle: its written language, dubbed “Trunic” by its fans. Several hours was actually _less_ than I expected it to take! And figuring out the answer was satisfying and I immediately wanted to write something in Trunic myself.

![(Which I have represented here as a screenshot without useful alt text so it doesn't become an unwanted hint.)](https://belkadan.com/blog/2024/07/Trunic/bark.png)

[Tunic](https://tunicgame.com) is a game from a few years ago with the aesthetics of a top-down Zelda and the combat of a light Souls-like. But it’s also built on puzzles and hidden lore, and a significant part of that is that most of the game is in some mysterious language, with only bits and pieces of normal English poking through. (Also the [soundtrack](https://lifeformed.bandcamp.com/album/tunic-original-game-soundtrack) is great.)

You can play all of Tunic and get the “true ending” without spending any effort on the language puzzle, treating it as part of the aesthetic. And indeed, it’d be a bunch harder to do the language puzzle without seeing the full (untranslated) instruction manual, but **even the untranslated manual has spoilers,** for reasons that will be obvious not long into a new game. So if this sounds like a game you might play, I’d suggest _not_ going to look up the manual online just to take a crack at this puzzle.

(Aside: I didn’t actually play the game; I was worried about it exacerbating my wrist RSI. Instead, I watched [MasaeAnela](https://www.twitch.tv/masaeanela) play through it, a sunny, wholesome streamer who I was already following. Watching someone stream a _puzzle-based_ game can sometimes be frustrating when you solve the puzzle before they do, but that didn’t happen too often, and to be fair I probably would have flopped the combat a lot more than Masae did.)

One thing I noticed after solving the puzzle is how hard it is to give hints without giving the whole thing away. So I sat down and made a list of hints, in order from “least revealing” to “most revealing” (except the last few, which are for once you’ve gotten the “big insight” and are filling out the solution). To help people who instinctively click on spoilers (or are using reader mode, they’re written in [rot13](https://rot13.com) (which that link will decode for you). If you’re stuck, see if _one_ hint can get you unstuck before going on to the next!

If you solve the puzzle, know that people have made generators for Trunic! Go search for one and send me a message, as a picture. (But don’t do it _before_ you solve the puzzle, because the instructions on how to use the generators would give you the answer.)

**Once you have solved the puzzle, you can find more thoughts on the construction of Trunic by (1) translating the first word of the Trunic above, and (2) putting that at the end of the full URL of this blog post on belkadan.com, after the final slash.**

- Gur chmmyr tbqf, re, tnzr qrif jrer trarebhf va tvivat hf *fcnprf.* Znxr hfr bs gung!
- Va cnegvphyne, svaq fbzr jbeqf gung lbh unir thrffrf sbe gur zrnavat bs. Gung’f evtug! Guebj bhg gur jevgvat flfgrz sbe abj, vg zvtug or urycshy yngre, ohg lbhe svefg tbny vf whfg gb svaq jbeqf.
- V erpbzzraq qbvat *fubeg* jbeqf svefg. Guvf vf na vafgvapg sebz Npghny Pbyyrtr Yvathvfgvpf Pynffrf: fubeg jbeqf ner hfhnyyl rvgure tenzzngvpny va angher (yvxr “jvyy” naq “abg”) be eryngviryl fvzcyr/pbzzba jbeqf (yvxr “qbt” naq “tb”), orpnhfr gubfr ner gur barf gung trg hfrq serdhragyl rabhtu gb trg fubegrarq, be obgu. Guvf vfa’g n cresrpg urhevfgvp orpnhfr vg bayl pbafvqref fbzr jnlf jbeqf trg vairagrq (pbafvqre “wfba”), ohg vg’f fgvyy n tbbq fgnegvat cynpr. Lbh’er whfg pbyyrpgvat qngn evtug abj!
- Zl svefg vqragvsvrq jbeq jnf “gur”.
- Zl arkg vqragvsvrq jbeqf jrer “n”, “ner”, naq “svyr”, gubhtu jvgu yrff pregnvagl.
- Bapr lbh unir n pbyyrpgvba bs jbeqf jvgu ernfbanoyr pbasvqrapr, gel ybbxvat sbe fvzvynevgvrf orgjrra gurz.
- Guvf chmmyr vf zrnag gb or fbyirq jvgubhg sbezny yvathvfgvpf genvavat. Jung pna gur tnzr qrif nffhzr nobhg lbh, gur fbyire?
- Znxr fher gb cnl nggragvba gb gur unaqjevggra abgrf ba Gehavp ba n yngr znahny cntr. Vg fubhyq or pyrne gung guvf vf lbhe onfryvar gb jbex jvgu. (Vs lbh’er abg jbexvat jvgu gur shyy znahny, V jvyy fhzznevmr na vzcbegnag gnxrnjnl sebz guvf cntr va gur arkg uvag, ohg vg vf n ovt onfryvar fcbvyre!)
- Gur znva gnxrnjnl sebz gur cntr zragvbarq va gur cerivbhf uvag: gur jevgvat flfgrz vf onfrq ba gjb frcnengr frgf bs “tylcuf”, bar bs juvpu hfrf gur *obeqref* bs n urkntba, naq gur bgure bs juvpu vf flzobyf vafpevorq *jvguva* n urkntba.
- Gurer vf nabgure cntr jvgu unaqjevggra abgrf ba Gehavp gung’f abg va gur fnzr frpgvba. Lbh qba’g unir gb haqrefgnaq guvf bar vzzrqvngryl, ohg vg zvtug uryc gb xabj vg’f gurer.
- Gurer rkvfgf n fubeg qrfpevcgvba bs gur gjb vqragvsvrq “frgf” va gur jevgvat flfgrz. Vg’f n pbaprcg lbh nyernql haqrefgnaq.
- V jnf noyr gb svaq gung cnggrea onfrq fbyryl ba fubeg jbeqf.
- Snzvyvnevgl jvgu n aba-Ebzna, aba-Plevyyvp jevgvat flfgrz jvyy yvxryl tvir lbh na nqinagntr (ohg gurer ner n ybg bs jevgvat flfgrzf va gur jbeyq, fb fbzr cebonoyl jba’g).
- Gurer ner *fbzr* cnggreaf *jvguva* gur gjb vqragvsvrq “frgf” bs gur jevgvat flfgrz. Guvf urycf gb abg or svthevat gurz bhg bar-ol-bar, naq jura lbh’er svthevat bhg gur ynfg srj, lbh pna thrff jung vg *zvtug* or naq gura tb ybbx sbe n cynpr vg bhtug gb or hfrq.
- Vs lbh raq hc jvgu gur fnzr ynfg bar nf zr, vg’f ba cntr 26.

This entry was posted on [July](https://belkadan.com/blog/2024/07) 17, [2024](https://belkadan.com/blog/2024) and is filed under [Personal](https://belkadan.com/blog/personal). Tags: [Games](https://belkadan.com/blog/tags/games)
