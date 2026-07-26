---
title: 'Color Palette #8'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2018/01/Color-Palette-8/'
original_language: en
published: 2018-01-29
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:9dcb2dbcf7769033'
translated: false
---

> 原文：[Color Palette #8](https://belkadan.com/blog/2018/01/Color-Palette-8/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/)

[Many-to-Many Protocols](https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/) »

[Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=mac-os-classic) »

[The Biggest Smallest PNG](https://belkadan.com/blog/2024/01/The-Biggest-Smallest-PNG/?tag=graphics) »

## [Color Palette #8](#)

A few days ago I was poking around the resources for a good old Mac game, [Maelstrom](https://www.libsdl.org/projects/Maelstrom/). The port to Mac OS X (now just “macOS”) mostly left the resources of the old game in their original format, the Macintosh “[resource fork](https://en.wikipedia.org/wiki/Resource_fork)”; the only difference is that it stores the resources as normal data instead of in the special part of the filesystem where they used to live.more

I didn’t have any particular goals in mind, but I happened to open one of the old sprites in a hex editor, and

[![...a sprite for a spaceship that uses 8-bit pixels looks like a spaceship when viewed in a hex editor.](https://belkadan.com/blog/2018/01/Color-Palette-8/spaceship.png)](https://twitter.com/UINT_MIN/status/956390109540044800)

!!

Twitter user Félix Fischer‏ [suggested adding “syntax” coloring](https://twitter.com/FelixFischer91/status/956515456302624769) to make the picture more clear. But if I was going to do that, I might as well use the original colors…

These days, the way computers represent colors, at least at a high level, is a set of three decimal numbers representing the amount of “red”, “green”, and “blue”.[1](#fn:hsv) The “correct” way to think about these numbers is as coordinates in some kind of three-dimensional space, but the quick-and-dirty way is to imagine three different colored lights set to different brightnesses, with 0.0 as “completely off” and 1.0 as “completely on”. If you remember your elementary school science classes, mixing red, green, and blue light creates white, or an approximation of white anyway, because of how human eyes work.

But once upon a time, computers had really limited storage space, and representing images with full color values, or even an integer approximation, was too expensive. So they would use _color palettes_ instead. Instead of saying “this pixel is `(red: 0.0, green: 1.0, blue: 0.0)`”, you’d say “this pixel is color #3”. The mappings of colors could be baked into the operating system or even the hardware, or they could be [swappable at runtime](http://www.effectgames.com/demos/canvascycle/?sound=0).

In this case, the sprites from Maelstrom were using Macintosh color lookup table (“`clut`”) #8, the standard “256-color” palette from the early days of 256-color Mac OS. (Fun fact: it’s #8 because it’s the standard color palette for “8-bit” images. There’s also a #4 palette for 4-bit images—16 colors.) That palette offers a pretty good spread of colors by handling a mix of red, green, and blue values in the range 0…5, then adding solid red, green, blue, and grey values in the range 0…15, _minus_ the multiples of 3. Why minus the multiples of three? Because you can already get those from the red+green+blue composite colors. That palette looks like this:

[![(as seen in Mac OS Classic!)](https://belkadan.com/blog/2018/01/Color-Palette-8//clut8.png)](https://twitter.com/uliwitness/status/957060846802341889)

And here’s a computational representation:

```
func clut8ColorComponents(index x: UInt8)
    -> (red: Double, green: Double, blue: Double) {
  if x < 215 {
    // Component-based colors, with RGB values in the range 0...5,
    // stored in reverse order (i.e. color #0 is white, (1.0, 1.0, 1.0)).
    // Note that x == 215 would normally produce black, (0.0, 0.0, 0.0),
    // but the palette deliberately puts that at the end.
    let red   = Double(5 - (x / 36))    / 5.0
    let green = Double(5 - (x / 6 % 6)) / 5.0
    let blue  = Double(5 - (x % 6))     / 5.0
    return (red: red, green: green, blue: blue)
  
  } else if x == 255 {
    // Special case: black is last.
    return (red: 0.0, green: 0.0, blue: 0.0)
  
  } else {
    // Extra shades of "primary" colors: red, green, blue, and grey.
    let values = (0...15).reversed()
                         .filter { $0 % 3 != 0 }
                         .map { Double($0) / 15.0 }
    assert(values.count == 10)
  
    let which = Int((x - 215) % 10)
    switch (x - 215) / 10 {
    case 0: return (red: values[which], green: 0.0, blue: 0.0)
    case 1: return (red: 0.0, green: values[which], blue: 0.0)
    case 2: return (red: 0.0, green: 0.0, blue: values[which])
    case 3: return (red:   values[which],
                    green: values[which],
                    blue:  values[which])
    default: fatalError("x must be out of range")
    }
  }
}
```

And since I had to go through some minor trouble extracting it, [**here’s a copy of that color palette**](https://belkadan.com/blog/2018/01/Color-Palette-8/clut8.r) in Rez resource description form. Thanks to suggestions from [Uli Kusterer](https://twitter.com/uliwitness/status/957061749685047297), [Peter Hosey](https://twitter.com/boredzo/status/957072683803406336), and [Jonathan Grynspan](https://twitter.com/grynspan/status/957080155507261440) on where to go looking for it.

P.S. Since [Hex Fiend](http://www.ridiculousfish.com/hexfiend/) is open source, I was [actually able to add the colors](https://twitter.com/UINT_MIN/status/956760154308952066) in the end, although that picture comes from eyeballing the color palette I found [on the 2002 website for the book _Web Style Guide_](http://webstyleguide.com/wsg2/graphics/safe.html) rather than using the real colors. But it’s close enough.

1. There are a number of other representations as well; I happen to prefer [hue-saturation-value](https://en.wikipedia.org/wiki/HSL_and_HSV). But since _screens_ are still based on red-green-blue values, that’s what I’m going to talk about here. (Of course, printers are not, since they have to mix ink instead of light.) [↩︎](#fnref:hsv)

This entry was posted on [January](https://belkadan.com/blog/2018/01) 29, [2018](https://belkadan.com/blog/2018) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic), [Graphics](https://belkadan.com/blog/tags/graphics)
