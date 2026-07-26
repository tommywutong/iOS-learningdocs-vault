---
title: Quick Look Debugging
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/quick-look-debugging/'
original_language: en
published: 2015-03-30
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:4a96b9873850bd58'
translated: false
---

> 原文：[Quick Look Debugging](https://nshipster.com/quick-look-debugging/)　·　NSHipster (Mattt)

# [Quick Look Debugging](https://nshipster.com/quick-look-debugging/)

Written by  [Nate Cook](https://nshipster.com/authors/nate-cook/)  March 30^th, 2015

Debugging can be an exercise in irony. We create programs that tell our pint-sized supercomputers to complete infinitely varied and incalculable tasks on our behalf, yet when trying to understand those same programs, we tell the computers to wait for _us._

For example, suppose I’m trying to figure out why the `UINavigationBar` in my app doesn’t appear as I expected. To investigate, I might use the debugger to look at the `UIColor` instance I’m setting on the navigation bar—what color _is_ this, exactly?

![UIColor in Debug](https://nshipster.com/assets/quicklook-debug-90b953d443516f9a0c0cbd5d7a0a9afeed8b100b0f3295a88435970897d7dab0e5dad86deb94fe32bfe2bb06d39f894b6113a70e87f10b8dc08c4cf14a9a4b6b.gif)

Hold on! No more trying to figure out how those components add together. _There’s a better way._

Since version 5, Xcode has shipped with Quick Look display in the debugger. Just as you can inspect the contents of a file on the Desktop with a quick tap of the space bar, in Xcode you can use Quick Look to see a visual representation of a variety of datatypes. Tapping the space bar on our `color` variable gives an instant answer—no off-the-top-of-your-head RGB calculations required:

![UIColor Quick Look](https://nshipster.com/assets/quicklook-color-d1e9b3a7ef497fb7cc3b2f90a35d5a86df7b9b74ac59cb368cb030d4ff96e052e6eff7594e296a1391bed57eaa1c032da8c1993ae92d0d98e5c472a63ef2ee72.gif)

---

You can also invoke Quick Look while debugging directly from your code. Consider the following method, `buildPathWithRadius(_:steps:loopCount:)`. It creates a `UIBezierPath` of some kind, but you’ve forgotten which, and does this code even work?

```
func buildPathWithRadius(radius: CGFloat, steps: CGFloat, loopCount: CGFloat) -> UIBezierPath {
    let away = radius / steps
    let around = loopCount / steps * 2 * CGFloat(M_PI)
    
    let points = map(stride(from: 1, through: steps, by: 1)) { step -> CGPoint in
        let x = cos(step * around) * step * away
        let y = sin(step * around) * step * away
        
        return CGPoint(x: x, y: y)
    }
    
    let path = UIBezierPath()
    path.moveToPoint(CGPoint.zeroPoint)
    for point in points {
        path.addLineToPoint(point)
    }
    
    return path
}
```

```
- (UIBezierPath *)buildPathWithRadius:(CGFloat)radius steps:(CGFloat)steps loopCount:(CGFloat)loopCount {
    CGFloat x, y;
    CGFloat away = radius / steps;
    CGFloat around = loopCount / steps * 2 * M_PI;
    
    UIBezierPath *path = [UIBezierPath bezierPath];
    [path moveToPoint:CGPointZero];
    
    for (int i = 1; i <= steps; i++) {
        x = cos(i * around) * i * away;
        y = sin(i * around) * i * away;
        
        [path addLineToPoint:CGPointMake(x, y)];
    }
    
    return path;
}
```

To see the result, you could surely create a custom view for the bezier path or draw it into a `UIImage`. But better yet, you could insert a breakpoint at the end of the method and mouse over `path`:

![Spiral UIBezierPath Quick Look](https://nshipster.com/assets/quicklook-spiral-ae59f476054a09af2172bcc5df458cac8bc8b1f94ae9e5fc72a0a9404461d103b19b1c38791e94cfb4557aef426de1d543b5852b4303860831e12a73c0267f30.gif)

Spiraltastic!

---

### Built-In Types

Quick Look can be used with most of the datatypes you’ll want to visualize right out of the box. Xcode already has you covered for the following types:

> - **Images:**`UIImage`, `NSImage`, `UIImageView`, `NSImageView`, `CIImage`, and `NSBitmapImageRep` are all visible via Quick Look.
> - **Colors:**`UIColor` and `NSColor`. (Sorry, `CGColor`.)
> - **Strings:**`NSString` and `NSAttributedString`.
> - **Geometry:**`UIBezierPath` and `NSBezierPath` along with `CGPoint`, `CGRect`, and `CGSize`.
> - **Locations:**`CLLocation` gives a large, interactive view of the mapped location, with details about altitude and accuracy in an overlay.
> - **URLs:**`NSURL` is represented by a view showing the local or remote content addressed by the URL.
> - **Cursors:**`NSCursor`, for the cursored among us.
> - **SpriteKit:**`SKSpriteNode`, `SKShapeNode`, `SKTexture`, and `SKTextureAtlas` are all represented.
> - **Data:**`NSData` has a great view showing hex and ASCII values with their offset.
> - **Views:** Last but not least, any `UIView` subclass will display its contents in a Quick Look popup—so convenient.

What’s more, these Quick Look popups often include a button that will open the content in a related application. Image data (as well as views, cursors, and SpriteKit types) offer an option to open in Preview. Remote URLs can be opened in Safari; local ones can be opened in the related application. Finally, plain-text and attributed string data can likewise be opened in TextEdit.

### Custom Types

For anything beyond these built-in types, Xcode 6 has added Quick Look for custom objects. The implementation couldn’t be simpler—add a single `debugQuickLookObject()` method to any `NSObject`-derived class, and you’re set. `debugQuickLookObject()` can then return any of the built-in types described above, configured for your custom type’s needs:

```
func debugQuickLookObject() -> AnyObject {
    let path = buildPathWithRadius(radius, steps: steps, loopCount: loopCount)
    return path
}
```

```
- (id)debugQuickLookObject {
    UIBezierPath *path = [self buildPathWithRadius:self.radius steps:self.steps loopCount:self.loopCount];
    return path;
}
```

---

In sum, Quick Look enables a more direct relationship with the data we manipulate in our code by allowing us to iterate over smaller pieces of functionality. This direct view into previously obfuscated datatypes brings some of the immediacy of a Swift Playground right into our main codebase. Displaying images? Visualizing data? Rendering text? Computers are so good at all that! Let’s let them do it from now on.
