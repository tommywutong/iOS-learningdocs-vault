---
title: Adding a background to your view
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/adding-a-background-to-your-view
source_url: 'https://developer.apple.com/documentation/swiftui/adding-a-background-to-your-view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/adding-a-background-to-your-view.json'
content_hash: 'sha256:01250ef423e75d0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Layout fundamentals](layout-fundamentals.md)

# Adding a background to your view

<sub>Article</sub>

Compose a background behind your view and extend it beyond the safe area insets.

## Overview

You can add a view as a background with the [background(alignment:content:)](<view/background(alignment_content_).md>) view modifier. To add a background under multiple views, or to have a background larger than an existing view, you can layer the views by placing them within a [ZStack](zstack.md), and place the view you want to be in the background at the bottom of the view stack. You can specify that a background view should ignore the safe area insets to extend the background to some or all edges.

### Add a background

If your design calls for a background, you can use the [background(alignment:content:)](<view/background(alignment_content_).md>) modifier to add it underneath an existing view. The following example adds a gradient to the vertical stack using the [background(alignment:content:)](<view/background(alignment_content_).md>) view modifier:

```swift
let backgroundGradient = LinearGradient(
    colors: [Color.red, Color.blue],
    startPoint: .top, endPoint: .bottom)

struct SignInView: View {
    @State private var name: String = ""

    var body: some View {
        VStack {
            Text("Welcome")
                .font(.title)
            HStack {
                TextField("Your name?", text: $name)
                    .textFieldStyle(.roundedBorder)
                Button(action: {}, label: {
                    Image(systemName: "arrow.right.square")
                        .font(.title)
                })
            }
            .padding()
        }
        .background {
            backgroundGradient
        }
    }
}
```

The [background(alignment:content:)](<view/background(alignment_content_).md>) view modifier constrains the size of the background view to be the same size as the view to which it’s attached:

![](../../../attachments/0bf57a769f3fffece6ad3746e6189c9b/Adding-a-Background-to-Your-View-1@2x.png)

<sub>A screenshot of an iPhone showing a gradient background for the welcome title, text field, and button in the horizontal stack, not filling in the rest of the phone’s background.</sub>

### Expand the background underneath your view

To create a background that’s larger than the vertical stack, use a different technique. You could add [Spacer](spacer.md) views above and below the content in the [VStack](vstack.md) to expand it, but that would also expand the size of the stack, possibly changing it’s layout. To add in a larger background without changing the size of the stack, nest the views within a [ZStack](zstack.md) to layer the [VStack](vstack.md) over the background view:

```swift
struct SignInView: View {
    @State private var name: String = ""

    var body: some View {
        ZStack {
            backgroundGradient
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
    }
}
```

View sizes within a depth stack are independent, unlike when using the background view modifier. The view from [Gradient](gradient.md) expands to fill the space available to the stack, but avoids the safe area insets by default:

![](../../../attachments/28c3048a58718732a59c8d93b16cf7eb/Adding-a-Background-to-Your-View-2@2x.png)

<sub>A screenshot of an iPhone showing a gradient background filling almost all of the background, excluding the top status bar and the bottom bar.</sub>

For more information on usings stacks to combine views, see [Building layouts with stack views](building-layouts-with-stack-views.md).

### Extend the background into the safe areas

By default, SwiftUI sizes and positions views to avoid system defined safe areas to ensure that system content or the edges of the device won’t obstruct your views. If your design calls for the background to extend to the screen edges, use the [ignoresSafeArea(_:edges:)](<view/ignoressafearea(__edges_).md>) modifier to override the default.

```swift
struct SignInView: View {
    @State private var name: String = ""
    var body: some View {
        ZStack {
            backgroundGradient
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
        .ignoresSafeArea()
    }
}
```

The background gradient fills the display area of the device and ignores the safe area insets.

![A screenshot of an iPhone showing a gradient background filling the entire background.](../../../attachments/412380a0db85bd69c4d78c41bc8bf147/Adding-a-Background-to-Your-View-3@2x.png)

### Adjust views when displaying the keyboard

You can ignore the keyboard’s safe area by adding the [ignoresSafeArea(_:edges:)](<view/ignoressafearea(__edges_).md>) modifier. When you activate the keyboard, the content of the vertical stack remains fixed, ignoring the space used by the keyboard:

![](../../../attachments/dbcdefbeadfd2a3fd95589b4e72b7eb6/Adding-a-Background-to-Your-View-4@2x.png)

<sub>A screenshot of an iPhone showing a gradient background filling the entire background, with the keyboard overlaid at the bottom of the screen. The welcome title, text field, and button within the horizontal stack are centered between the top and bottom of the iPhone, with the keyboard obscuring the lower portion of the background.</sub>

To get the contents of the vertical stack to respect the safe areas and adjust to the keyboard, move the modifier to only apply to the background view.

```swift
struct SignInView: View {
    @State private var name: String = ""
    var body: some View {
        ZStack {
            backgroundGradient
                .ignoresSafeArea()
            VStack {
                Text("Welcome")
                    .font(.title)
                HStack {
                    TextField("Your name?", text: $name)
                        .textFieldStyle(.roundedBorder)
                    Button(action: {}, label: {
                        Image(systemName: "arrow.right.square")
                            .font(.title)
                    })
                }
                .padding()
            }
        }
    }
}
```

To accommodate the keyboard, SwiftUI resizes and positions your view. Because the background view has the [ignoresSafeArea(_:edges:)](<view/ignoressafearea(__edges_).md>) modifier, it remains unchanged.

![](../../../attachments/6efd7980ea4347e5b74de09f0907c406/Adding-a-Background-to-Your-View-5@2x.png)

<sub>A screenshot of an iPhone showing a gradient background filling the entire background, with the keyboard overlaid at the bottom of the screen. The welcome title, text field, and button within the horizontal stack is centered between the top of the keyboard and the top of the iPhone, and the gradient background extends underneath the keyboard for the full height of the iPhone.</sub>

## See Also

### Layering views

- [ZStack](zstack.md) — A view that overlays its subviews, aligning them in both axes.
- [zIndex(_:)](<view/zindex(__).md>) — Controls the display order of overlapping views.
- [background(alignment:content:)](<view/background(alignment_content_).md>) — Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](<view/background(__ignoressafeareaedges_).md>) — Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](<view/background(ignoressafeareaedges_).md>) — Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](<view/background(__in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](<view/background(in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with the default background style.
- [overlay(alignment:content:)](<view/overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](<view/overlay(__ignoressafeareaedges_).md>) — Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](<view/overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [backgroundMaterial](environmentvalues/backgroundmaterial.md) — The material underneath the current view.
- [containerBackground(_:for:)](<view/containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](<view/containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
- [ContainerBackgroundPlacement](containerbackgroundplacement.md) — The placement of a container background.
