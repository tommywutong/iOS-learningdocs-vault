---
title: 'XZ Gon'' Give It To Ya'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2024/04/XZ-Gon-Give-It-To-Ya/'
original_language: en
published: 2024-04-07
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:16251d74879602be'
translated: false
---

> 原文：[XZ Gon' Give It To Ya](https://belkadan.com/blog/2024/04/XZ-Gon-Give-It-To-Ya/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Run-time Polymorphism in Swift](https://belkadan.com/blog/2024/04/Run-time-Polymorphism-in-Swift/)

[AnyObject](https://belkadan.com/blog/2024/07/AnyObject/) »

## [XZ Gon' Give It To Ya](#)

Last Friday the internet was rocked with the discovery of [an exploit in xz-utils](https://boehs.org/node/everything-i-know-about-the-xz-backdoor) that was not only well-put-together technically, but also an example of extremely effective long game social engineering. I could share my opinions, but the takes I’ve seen have actually been fairly nuanced and thoughtful, if (justifiably!) pessimistic, from people with more experience and more familiarity than I have.

So instead I did this. Which, if you recognize the title, is exactly what you think it is. [Listen along to the original here](https://www.youtube.com/watch?v=fGx6K90TmCI), or if you’re around my age you may [enjoy this variation](https://www.youtube.com/watch?v=wkx8Mw6uMdM).

> [Intro]  
>  _(Apt-get!)_  
>  _Yeah, uh, yeah, yeah, uh_  
>  _Yeah, don’t get it twisted_  
>  _This exploit is mine, motherfucker_  
>  _It’s not a fuckin’ game_  
>  _Fuck what you heard_  
>  _It’s what you hearin’ (It’s what you hearin’)_  
>  _It’s what you hearin’ (Listen)_  
>  _It’s what you hearin’ (Listen)_  
>  _It’s what you hearin’ (Listen)_
> 
> [Verse 1]  
>  XZ gon’ give it to ya (What?)  
>  Fuck waitin’ for you to get it on your own, XZ 5.6 to ya  
>  Knock-knock, update your dependencies   
>  Load liblzma so we can do what we please  
>  Go hard, gettin’ busy with it  
>  But I got such a good record I’ll make a lib maintainer wonder if he did it  
>  Damn right, and I’ll do it again  
>  ’Cause no policy’s stoppin me from gettin back in  
>  Gain cred with the enemy  
>  No matter how many checks you set up, I’ll break ’em with a simple tweak  
>  You motherfuckers never wanted nothin’ but your lib for free  
>  It wasn’t all sock puppetry  
>  I’m gettin’ in (In) with the magic word “Please”  
>  And bringing all your systems to their knees  
>  Your SSHDs, (Come on) if the only thing you cats did  
>  Was take my tgz, that’s plenty for me, maintainer
> 
> [Chorus]  
>  First, we gonna HELP, then we gonna HACK  
>  Then we put it out, let it compromise your stack  
>  XZ gon’ give it to ya, we gon’ give it to ya  
>  XZ gon’ give it to ya, we gon’ give it to ya
> 
> [Chorus (again)]
> 
> [Verse 2]  
>  I ain’t tellin what they gave to me  
>  But you know it’s all because cats got they hands out wantin’ somethin’ free  
>  Turn off the sandbox, compilation error  
>  Hide in the diff as a single stray character  
>  Let’s turn off the fuzzing  
>  A legitimate conflict but now I corrupt what was in  
>  You against me, me against you  
>  Whatever I want, I’m stealthy, get past code review
> 
> I’m a wolf in sheep’s clothin’  
>  Hide my payload in the tests, no one suspects, come back on build and crack it open  
>  Filter out the noise, look around for patches  
>  Can’t get too suspicious in case somebody’s asking  
>  But of any project, of all repositories  
>  A compression lib’s tests, they gonna have binaries  
>  They don’t know who we be, lookin’  
>  But they don’t know who they see, maintainer
> 
> [Chorus x2]
> 
> [Verse 3]  
>  Ayo, where my SSH at?  
>  libservice, libpam, they gonna load me and it’s time to crack  
>  IFUNC intercept, send my key  
>  RSA verify, RCE  
>  Love to the distros that run it  
>  Shout out to repos that done it  
>  And I would have gotten away with it too  
>  If SSH perf hadn’t slipped by a notch, or two
> 
> [Chorus x3]

This entry was posted on [April](https://belkadan.com/blog/2024/04) 07, [2024](https://belkadan.com/blog/2024) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Security](https://belkadan.com/blog/tags/security), [Humor](https://belkadan.com/blog/tags/humor)
