---
title: Reverse Engineering Stickies.app - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/reverse-engineering-stickies.app/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5b03182561f8b53f'
translated: false
---

> 原文：[Reverse Engineering Stickies.app - Low Level Bits 🇺🇦](https://lowlevelbits.org/reverse-engineering-stickies.app/)　·　Low Level Bits (Alex Denisov)

# Reverse Engineering Stickies.app

_Published on Feb 13, 2017_

Recently I have discovered the nice Stickies app that comes along with OS X. This is exactly what I needed for making quick notes while watching lectures or during debug sessions.

However, the first thing I did when I run the app first time - I opened preferences attempting to change the colors of notes. But there are no preferences, and there is no way to use a color other than six predefined.

I decided to fix that. Here is the result:

![](https://lowlevelbits.org/img/reverse-engineering-stickies/before_after.png)

![](https://lowlevelbits.org/img/reverse-engineering-stickies/colors.png)

The explanation is following.

### Reversing UI

The task becomes easy since the six colors are hardcoded in the binary. I just need to find where exactly and change the values to ones I like more.

I don’t know where to start, but I have an idea.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/menu_before.png)

The colors are listed in the menu. Each color has a name next to an icon. The names should be localized using some string as a key. If I can find the key, then I can get the place where it’s used. Maybe then I will get another hint.

Localizations are stored within the app’s bundle, at `Contents/Resources` folder. I am particularly interested in `Contents/Resources/English.lproj/Localizable.strings`. By default, strings are Binary Plists. One can use `plutil` to convert them into human-readable XML:

```bash
plutil -convert xml1 Contents/Resources/English.lproj/Localizable.strings
```

The `Localizable.strings` contains many things, but colors are not there.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/localizable_strings.png)

It looks like the menu was created using Interface Builder.

Indeed, there is a menu and a view for a sticky note as well:

![](https://lowlevelbits.org/img/reverse-engineering-stickies/ls_nibs.png)

As far as I know nib files used to have some proprietary binary format. Nowadays, however, they are just Binary Plists, which are easy to convert into XML:

```bash
plutil -convert xml1 Contents/Resources/Base.lproj/MainMenu.nib
```

Unlikely that I can find something useful inside, but let’s see. The `MainMenu` contains 20k lines. Also, it is quite cryptic:

![](https://lowlevelbits.org/img/reverse-engineering-stickies/main_menu_nib.png)

The best thing one can do is to try find something. For instance look for a color name:

![](https://lowlevelbits.org/img/reverse-engineering-stickies/main_menu_nib_color.png)

If I replace “Blue” with “Blur” and restart the app, then I see the change:

![](https://lowlevelbits.org/img/reverse-engineering-stickies/menu_color_name_changed.png)

Ok, I can modify menu entries. It doesn’t help me to achieve the initial goal, but at least I know where to look at if I ever decide to change a menu.

### Reversing Code

My attempt to find traces from UI has failed. What’s left? The binary itself!

I usually use [MachOView](https://sourceforge.net/projects/machoview/) if I need to look into a binary. Let’s see if I can find a method related to the colors.

Search for “blue” shows one hit `colorWithDeviceRed:green:blue:alpha:` that comes from AppKit’s `NSColor` class. Search for “yellow” and other colors gives no results.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/machoview.png)

It feels like a dead end.

Instead of searching for other words hoping that I will find something useful I can ask [class-dump](https://github.com/nygard/class-dump) for help.

```bash
class-dump Contents/MacOS/Stickies > Stickies.h
```

Shallow look at `Stickies.h` shows that class `StickiesWindow` has a method `setColorByIndex:`.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/stickies_window.png)

Perfect. It looks like this method receives an index of a color from the menu.

Let’s explore the program in the wild.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/lldb_no_location.png)

Hm, what does it mean? Why can’t LLDB find the symbol? Eventually, I left the questions open.

Then I decided to look at the binary through the excellent [Hopper app](https://www.hopperapp.com).

The Hopper app has a beautiful feature: pseudo-code mode.

It (almost) clearly shows what happens inside of `setColorByIndex:` method:

![](https://lowlevelbits.org/img/reverse-engineering-stickies/hopper_pseudo_code.png)

`r14` contains a color index. Then, based on this index some offset is calculated. If an index is zero, then the offset is zero as well. Hence we can ignore it at this stage.

What is important here: three consecutive values starting at `0x10000c790` moved to `xmm_` registers. I’m not 100% sure, but I’d assume that they are used to pass parameters into `colorWithDeviceRed:green:blue:alpha:`.

The method accepts color components as `double`s, where 0 corresponds to 0, and 1 corresponds to 255. An interval between the values - 8 bytes, which perfectly fits into a `double`.

It looks like these are exactly the colors I am looking for. This pattern repeats four times, meaning that four colors are used to colorize a sticky note view.

Let’s use lldb to confirm the hypothesis.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/lldb_color_values.png)

So, I found the following address/value pairs:

```
0x10000c790 : 0.99607800000000002 (or 254)
0x10000c798 : 0.95686199999999999 (or 244)
0x10000c7a0 : 0.61176399999999997 (or 156)
```

I’m pretty sure I’m done here, but one more check, just to make sure there is no mistake.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/color_picker.png)

Perfect! Now I need to patch the binary and change the values.

### Patching The Binary

Now I know where the colors reside in code. I need to find them in the binary. The address of a first color component is 0x10000c790. To find its on-disk address I need to subtract a base address from it. The base address can be obtained via LLDB as well.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/lldb_base_address.png)

Little math:

```
0x10000c790 - 0x0000000100000000 = 0xc790
```

Now I can use xxd with -s (`--seek`) and -l (`--length`) parameters to get exactly 8 bytes at a given address.

![](https://lowlevelbits.org/img/reverse-engineering-stickies/xxd_color_value.png)

In this case, these bytes are: `9a7b 48f8 dedf ef3f`. Guess what I would see if I write 0.99607800000000002 into a file? Exactly, I’d see `9a7b 48f8 dedf ef3f` there.

Now I can pick value I want to use and start writing them one by one starting at `0xc790`. But I have a better idea.

Let’s recall and rewrite a pseudo-code from Hopper:

```c
base = 0xc790;
r = base + 0;
g = base + 8;
b = base + 16;
color1 = rgb(r, g, b);
r = base + 24;
g = base + 32;
b = base + 40;
color2 = rgb(r, g, b);
r = base + 48;
g = base + 56;
b = base + 64;
color3 = rgb(r, g, b);
r = base + 72;
g = base + 80;
b = base + 88;
color4 = rgb(r, g, b);
```

This is a pseudo-code to handle one group of colors, the Yellow group. Code for the next group, Blue, will be almost the same. One difference: base address.

Here where the color index comes into play:

```c
base = (colorIndex + (colorIndex * 0x2)) << 0x5
```

Depending on the value of `colorIndex` it will give the following numbers:

```
0: 0
1: 96
2: 192
3: 288
4: 384
5: 480
```

The step is 96: this number of bytes is needed to store four colors. I don’t know how the source code looked initially, but I can represent it using the following structures:

```c
typedef struct {
  double red;
  double green;
  double blue;
} color;

typedef struct {
  color c1;
  color c2;
  color c3;
  color c4;
} theme;

/// One color theme for each color index
static theme themes[6] = {
 /// actual color definitions
};
```

I know that four colors are used, but I don’t yet know what they are used for. Patching them one by one gives the following result:

![](https://lowlevelbits.org/img/reverse-engineering-stickies/colored_window.png)

I can now rename field name to be more descriptive.

```c
typedef struct {
  color background_color;
  color border_color;
  color window_title_color;
  color icon_color;
} theme;
```

Once I have this in place changing the colors becomes a trivial task:

```c
color rgb(int r, int g, int b);
void changeColor(const int colorIndex, FILE *binary) {
  theme t;

  t.background_color = rgb(255, 255, 255);
  t.window_title_color = rgb(38, 173, 228);
  t.icon_color = t.window_title_color;
  t.border_color = rgb(77, 188, 233);

  const int ColorAddressBase = 0xc790;
  const int offset = ColorAddressBase + colorIndex * 96;
  fseek(binary, offset, SEEK_SET);
  fwrite(&t, sizeof(theme), 1, binary);
  rewind(binary);
}
```

After running this code, I see a much better Sticky Note!

![](https://lowlevelbits.org/img/reverse-engineering-stickies/blue_sticky.png)

### Summary

Reverse Engineering can be not as straightforward and easy as I described above. Indeed, I didn’t describe some ‘wrong’ paths I went through during this ‘research’. Here are few examples:

- I first was looking for integers instead doubles and could not make any sense out of it.
- I converted first double into hex, and it didn’t match one in the binary. Few hours later I realized that there must be different endianness, which was the case.
- I didn’t have to change the machine code. Otherwise, the process would be less pleasant - I would have to invalidate the whole Mach-O binary changing sizes of sections and offsets.

Anyway, I enjoyed this exercise and learned a few new things. So if you are in doubt, I can recommend following my instructions. Though, only for educational purposes!

Here are few helpful tips I can give:

- Work only with a copy of a program; it’s very easy to break things.
- Put everything under version control, and make commit after each small change. It will be easier to take another direction if you’re stuck.
- Make sure you preserve a size and a length if you change something. Otherwise, it may break the whole thing.

This is a list of tools that may be helpful for reverse engineering:

- [MachOView](https://sourceforge.net/projects/machoview/)
- [Hopper app](https://www.hopperapp.com)
- [class-dump](https://github.com/nygard/class-dump)
- lldb, xxd, plutil…

The code for this patch is on Github: [ModernStickies](https://github.com/AlexDenisov/ModernStickies).

Happy Hacking!
