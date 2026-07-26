---
title: Custom NSCells Done Right
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/custom-nscells-done-right.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a0eddd902c355d2d'
translated: false
---

> 原文：[Custom NSCells Done Right](https://www.mikeash.com/pyblog/custom-nscells-done-right.html)　·　mikeash.com Friday Q&A

Posted at 2006-04-06 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Making Xcode Better](https://www.mikeash.com/pyblog/making-xcode-better.html)  
Previous article: [Cocoa SIMBL Plugins](https://www.mikeash.com/pyblog/cocoa-simbl-plugins.html)  
Tags: [hack](https://www.mikeash.com/pyblog/?tag=hack) [nib](https://www.mikeash.com/pyblog/?tag=nib) [nscell](https://www.mikeash.com/pyblog/?tag=nscell)

Custom NSCells Done Right

by [Mike Ash](https://www.mikeash.com/)

Tonight I'm going to show you a simple class you can add to your project which will make everything Just Work.

NSControl has a very nice `+cellClass` method. You override that, and NSControl will automatically use your cell class when creating a new control. The problem arises because Interface Builder archives everything into your nib. When the nib is unarchived, you get whatever cell was archived into it. The problem is that you don't get your custom cell, you get the NSCell, even though you set a custom NSControl subclass. IB does not see your `+cellClass` override.

The solution is to take advantage of the coder and force it to do our will. NSKeyedUnrchiver, used to unarchive all 10.2+ nibs, has this useful method: `-setClass:forClassName:`. This lets you tell the unarchiver to hand back a different class than it stored. As you've probably guessed already, we're going to use this to make it give us an instance of our subclass.

You could stick a bit of code like this in your NSControl's `-initWithCoder:` method, but I'm aiming higher than that. I want to make this work right for _all_ of your subclasses, so you don't have to include extra code. You just do the obvious (override `+cellClass`) and it works.

To that end, we're going to subclass NSControl and then poseAsClass. We'll override `-initWithCoder:` to do our magic in a generic way, and then life is good.

We have to be careful, though, not to use the magic code in every circumstance. First, we'll fail gracefully on non-keyed coders. Then we want to make sure we're an actual NSControl subclass, so that we don't go mucking around with raw unsubclassed NSControls. We need to make sure that our superclass actually defines a cell class to begin with. And then we only need to perform the substitution if our cell class is different from super's. We'll stick these four conditions at the beginning of our method:

```
	BOOL sub = YES;
	
	sub = sub && [origCoder isKindOfClass: [NSKeyedUnarchiver class]]; // no support for 10.1 nibs
	sub = sub && ![self isMemberOfClass: [NSControl class]]; // no raw NSControls
	sub = sub && [[self superclass] cellClass] != nil; // need to have something to substitute
	sub = sub && [[self superclass] cellClass] != [[self class] cellClass]; // pointless if same
```

If any of those gives us NO then we just call super and we're done.

Assuming we pass all of the tests, then we get down to business. In case this archiver is used repeatedly, we want to make sure that our substitution is only in effect for us. We'll do that by getting the old class and saving it, then restoring it when we're finished decoding. Then we just substitute and call super. Here is the complete method:

```
- initWithCoder: (NSCoder *)origCoder
{
	BOOL sub = YES;
	
	sub = sub && [origCoder isKindOfClass: [NSKeyedUnarchiver class]]; // no support for 10.1 nibs
	sub = sub && ![self isMemberOfClass: [NSControl class]]; // no raw NSControls
	sub = sub && [[self superclass] cellClass] != nil; // need to have something to substitute
	sub = sub && [[self superclass] cellClass] != [[self class] cellClass]; // pointless if same
	
	if( !sub )
	{
		self = [super initWithCoder: origCoder]; 
	}
	else
	{
		NSKeyedUnarchiver *coder = (id)origCoder;
		
		// gather info about the superclass's cell and save the archiver's old mapping
		Class superCell = [[self superclass] cellClass];
		NSString *oldClassName = NSStringFromClass( superCell );
		Class oldClass = [coder classForClassName: oldClassName];
		if( !oldClass )
			oldClass = superCell;
		
		// override what comes out of the unarchiver
		[coder setClass: [[self class] cellClass] forClassName: oldClassName];
		
		// unarchive
		self = [super initWithCoder: coder];
		
		// set it back
		[coder setClass: oldClass forClassName: oldClassName];
	}
	
	return self;
}
```

Now we just have to make sure our class poses as NSControl:

```
+ (void)load
{
	[self poseAsClass: [NSControl class]];
}
```

Stick this all in an NSControl subclass called FixedNSControl (or whatever you prefer) and you're all set.

To test this, I created a very simple NSTextFiled subclass which basically does nothing but override `+cellClass`. It also overrides `-drawRect:` just to call super, so I have a convenient place to put a breakpoint. Here is MyTextField's source:

```
@interface MyTextFieldCell : NSTextFieldCell {} @end
@implementation MyTextFieldCell @end

@implementation MyTextField

+ (Class)cellClass
{
	return [MyTextFieldCell class];
}

- (void)drawRect: (NSRect)r
{
	[super drawRect: r];
}

@end
```

I put a breakpoint on `drawRect:` and tested the control's cell. Sure enough, it was my custom subclass:

```
(gdb) po [self cell]
<MyTextFieldCell: 0x32ed90>
```

Success! Now I can easily subclass NSControl and my custom cell follows right along, exactly as it always should have been.

Note: this code has not been thoroughly tested, use at your own risk, we are not responsible for any supernatural events arising due to its use, etc. etc.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/custom-nscells-done-right.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
