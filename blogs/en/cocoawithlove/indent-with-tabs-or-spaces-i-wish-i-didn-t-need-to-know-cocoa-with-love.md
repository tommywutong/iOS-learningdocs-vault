---
title: 'Indent with tabs or spaces? I wish I didn''t need to know. | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/04/01/neither-tabs-nor-spaces.html'
original_language: en
published: 2016-04-01
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:016f0b0817892018'
translated: false
---

> 原文：[Indent with tabs or spaces? I wish I didn't need to know. | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/04/01/neither-tabs-nor-spaces.html)　·　Cocoa with Love (Matt Gallagher)

The always entertaining [Erica Sadun](http://ericasadun.com) wrote an article on her blog yesterday about code indentation styles, titled [“Swift Style: Are you a 4-denter?”](http://ericasadun.com/2016/03/31/swift-style-are-you-a-4-denter/). There was [a flurry of replies on Twitter](https://twitter.com/ericasadun/status/715566210872582145) as others playfully chimed in.

While I love trolling and human misery as much as the next person, I’m always saddened when I see these discussions – not because I have a deeply vested interest in tabs over spaces or one indentation width over another – but because the existence of the argument reminds me of the fact that after more than 50 years of indented code, nothing has been done to fix the technology limitations that cause these debates.

Ignoring hypothetical technology changes to eliminate the problem, there are some code formatting choices you can make to maximize maintainability. But I’ll give you a hint: if you’re trying to save time by changing things on the left edge of the line, you’re looking in the wrong spot.

## A quick rhetorical question…

Have a look at the following code:

```swift
func helloWorld() {
   print("Hello world")
}
```

**Question**: when I typed this text, did I type Unix linefeeds `\n`, classic Mac carriage returns `\r` or Windows carriage return linefeeds `\r\n`?

Obviously, I didn’t type anything of the sort. I hit the “return” key and my text editor did whatever was required to take me to the start of the next line.

Here is how I feel about the encoding of layout commands:

> The encoding of layout commands is the responsibility of the text editor program, not the user. The fact that users are perpetually embroiled in debates about the underlying encoding is a failure between text editing programs and text formats to negotiate parameters without user intervention.

## Document formats could eliminate the debate entirely

Consider an XML document declaration:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

XML documents start by clearly declaring their type and encoding, eliminating ambiguity and making the potentially unsolvable problem of determining document type and [text encoding](https://www.cocoawithlove.com/blog/2016/04/01/(https:/en.wikipedia.org/wiki/Bush_hid_the_facts)) into a trivially easy task.

With a Swift file, knowing the format or text encoding is rarely a problem. Instead, imagine if it was standard practice for Swift documents to start with a comment like this:

```swift
/*swift tabwidth="4" prefertabs="true"*/
```

This shouldn’t be such a strange thing to see: something equvalent is probably buried in your .vimrc or Xcode settings. The problem is that this information is attached to your editor, not the document. This information needs to be carried along with the document.

If common code editors supported this type of “document declaration” comment, there wouldn’t need to be a tabs versus spaces debate. The mere presence of this line would be enough for a text editor to correctly interpret any combination of tab and space characters at the start of a line and ensure any newly added indentations are correctly encoded.

> Xcode _project_ files do include this type of declaration (File inspector → Text Settings). That’s great but Xcode doesn’t prevent you copying and pasting incorrect indents from another file, adding files to the project with the wrong indentation settings or simply adding spaces where they don’t belong. So the setting isn’t really an intrinsic part of the document, it’s just a guideline used when performing _some_ operations.

## Tabs versus spaces

But like I said before: in more than 50 years, no one in a position to fix the problem has done anything. I don’t anticipate change.

So given the existing constraints what do we do to keep editing and maintenance costs to a minimum? Tabs or spaces?

From a code maintenance point-of-view, it doesn’t really matter: you will need to vigilantly enforce your standard, no matter what standard you choose.

Both spaces and tabs require that all editors of a document coordinate on which standard they’re going to use. But tabs and spaces are both invisible by default which leads to mistakes. That’s the reason why hostility exists: it’s not because one is superior to another, it’s because anyone who uses a different standard to you is a potential looming threat to your coding standard.

Frankly, compilers should detect inconsistent indentation styles and emit warnings. That would help far more than any debate over choice of standard.

But detecting indentation is complicated by files where lines don’t always start on a whole number of indents…

## Non-indent formatting

There’s a related issue to indentation that requires separate discussion: horizontal alignment of text in ways other than indentation.

Non-indent formatting is one of the biggest reasons why many people choose spaces over tabs. For a range of reasons, tabs are more prone to problems when used as part of non-indent formatting.

Here’s my take on the issue though: you should never use non-indent formatting in your code, regardless of your choice of tabs or spaces for indentation encoding. This advice has little to do with tabs versus spaces though and more to do with the belief that time spent formatting code is time wasted and it creates an unncessary code maintenance headache.

I use the following rule and I suggest it for all people free to choose their own coding standards:

> **Indent code but _never_ horizontally align code in any other way**. After indentation, never put 2 spaces together (except inside a comment block or string literal) and never use a tab character at all.

Your editor may be set up to “smart indent” or otherwise facilitate certain kinds of non-indent formatting but I assure you, there’s still a non-zero effort involved in maintaing the aesthetic. It’s _much_ harder to coordinate this type of styling across a team than tabs/spaces settings. And it simply doesn’t help readability enough to be worth the effort.

### Hard wrapping and parameter alignment

Let’s look at some code to see what I’m talking about. Here’s some code from [Swift’s GenEnum.cpp](https://github.com/apple/swift/blob/master/lib/IRGen/GenEnum.cpp):

```cpp
void storeExtraInhabitant(IRGenFunction &IGF,
                          llvm::Value *index,
                          Address dest, SILType T) const override {
  auto &C = IGF.IGM.getLLVMContext();
  auto payloadTy = llvm::IntegerType::get(C,
                  cast<FixedTypeInfo>(TI)->getFixedSize().getValueInBits());
  dest = IGF.Builder.CreateBitCast(dest, payloadTy->getPointerTo());

  index = IGF.Builder.CreateZExtOrTrunc(index, payloadTy);
  index = IGF.Builder.CreateAdd(index,
            llvm::ConstantInt::get(payloadTy, ElementsWithNoPayload.size()));
  IGF.Builder.CreateStore(index, dest);
}
```

Clearly, this file is authored with a standard that requires parameters are horizontally aligned when they’re put on new lines. Is it really time well spent? The alignment plays poorly with the 80 character line width and many of the aligned parameters aren’t actually aligned – they just hang in the middle of the line for no apparent reason until you realize they’ve bumped up against the right margin of the window and been pushed partially leftwards.

Let’s look at this same code with no formatting other than indentation:

```cpp
void storeExtraInhabitant(IRGenFunction &IGF, llvm::Value *index, Address
   dest, SILType T) const override
{
   auto &C = IGF.IGM.getLLVMContext();
   auto payloadTy = llvm::IntegerType::get(C,
      cast<FixedTypeInfo>(TI)->getFixedSize().getValueInBits());
   dest = IGF.Builder.CreateBitCast(dest, payloadTy->getPointerTo());

   index = IGF.Builder.CreateZExtOrTrunc(index, payloadTy);
   index = IGF.Builder.CreateAdd(index, llvm::ConstantInt::get(payloadTy,
      ElementsWithNoPayload.size()));
   IGF.Builder.CreateStore(index, dest);
}
```

I’ve cheated slightly: I moved the opening brace to its own line and increased the indentation to 3 spaces. Both changes are to offset the increased density from eliminating non-indent formatting.

But despite my scurrilous cheating ways, I think there’s an objective truth here: the extensive formatting effort in the first example doesn’t make it substantially easier to read. In fact, I personally I find the more consistent indentation in the second example (the _lack_ of formatting) makes it _easier_ to read.

Even if you find the second example harder to read, you need to ask yourself: how much easier? Because the second example comes with a very big advantage: in Xcode (or [Vim](http://superuser.com/questions/72714/vim-line-wrap-with-indent#73190) and other editors), soft line wrapping with indentation can be automatic and completely eliminates any need to ever hard format code.

Relying on soft wrapping in your editor can take a little acclimatization (many developers have hard-wrapping techniques drilled into them) but this one approach alone can save dozens of hours of time per year as every edit, re-edit or refactor to a hard-wrapped line wastes a few seconds of your time.

### Column formatting

Maybe it was cruel to use C++ as an example: it’s ugly from the beginning. Let’s start with something that looks _pretty_. The following code is from [ffmpeg’s mpjpegdec.c](https://github.com/FFmpeg/FFmpeg/blob/master/libavformat/mpjpegdec.c):

```c
static const AVClass mpjpeg_demuxer_class = {
    .class_name     = "MPJPEG demuxer",
    .item_name      = av_default_item_name,
    .option         = mpjpeg_options,
    .version        = LIBAVUTIL_VERSION_INT,
};
```

Two columns! It looks pretty! It’s contextually appropriate for the declarative structure!

But are you really saving time? Separating the two columns helps you locate the right column more quickly but that’s not really very important.

```c
static const AVClass mpjpeg_demuxer_class = {
    .class_name = "MPJPEG demuxer",
    .item_name = av_default_item_name,
    .option = mpjpeg_options,
    .version = LIBAVUTIL_VERSION_INT,
};
```

Removing formatting has made the code uglier.

But you can still find the _keys_ at a glance, with almost the same speed. The right column doesn’t pop out and it doesn’t look like a pretty formatted table but there was no time wasted in lining up columns and no need for formatting maintenance.

Is your time really well spent by aligning columns?

## Conclusion

We shouldn’t need to care about tabs versus spaces – it should be coordinated between the document and the editor with no possibility for mistakes.

Sadly, that’s not how things work.

Compilers should emit warnings about inconsistent indentation used within a given file so we aren’t perpetually forced to police invisible characters.

Sadly, that’s not how things work, either.

Due to the failures of our tools to address the issue, we’re stuck with ongoing work to enforce whatever indentation standard we choose.

You can look at my code on Github and discover how I typically encode my indents. I do have a standard and I do keep to it but unless you choose to push changes to one of my projects, you shouldn’t care.

Far more interesting example to follow is how I handle whitespace _elsewhere_ on the line: a `\t` character will never appear anywhere except in an indent and two or more space characters will only appear in indents, comment blocks or string literals. This avoids a whole host of problems and combined with the fact that I use soft-wrapping where possible, saves a noticeable amount of time in editing and refactoring code.
