---
title: 为自定义 UIKit 视图添加 Writing Tools 支持
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-writing-tools-support-to-a-custom-uiview
source_url: 'https://developer.apple.com/documentation/uikit/adding-writing-tools-support-to-a-custom-uiview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-writing-tools-support-to-a-custom-uiview.json'
content_hash: 'sha256:99e85dada95bd9ae'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Writing Tools](writing-tools.md)

# 为自定义 UIKit 视图添加 Writing Tools 支持

<sub>文章</sub>

为你那些包含文本的自定义 iOS 视图添加 Writing Tools 支持，包括对行内替换动画的支持。

## 概述

如果你的 App 没有使用 [UITextView](uitextview.md) 或 [UITextField](uitextfield.md) 对象，你仍然可以为其他包含文本的视图添加 Writing Tools 支持。当你不想使用标准的文本视图时，可能会用到这种支持。例如，如果你使用 TextKit 或自己专有的文本引擎构建了自己的文本视图，就可能需要用到它。这项支持所对应的 UIKit API，让你能够访问与系统视图中相同的 Writing Tools 功能，包括为视图中文本的更改制作动画的能力。

当用户从你的自定义视图触发 Writing Tools UI 时，UIKit 会与你的视图协作，评估相关文本并整合更改。你需要为你的视图指定所需的 Writing Tools 体验类型。完整体验会直接为你视图内容的更改制作动画，与你的视图协作来创建这些动画。有限体验则在 Writing Tools UI 中显示更改，只将最终的更改整合回你视图的文本存储中。所有这些交互都是借助你附加到视图上的 [UIWritingToolsCoordinator](uiwritingtoolscoordinator.md) 对象完成的。

### 向视图添加 Writing Tools 协调器

[UIWritingToolsCoordinator](uiwritingtoolscoordinator.md) 对象管理你的视图与 Writing Tools 功能之间的交互。在 iOS 中，这个对象是一种 [UIInteraction](uiinteraction.md) 对象，只有当你想要支持 Writing Tools 时，才将它附加到你的视图上。为了管理视图特定的行为，你需要在设置协调器时提供一个委托对象。你的委托负责向 Writing Tools 提供待评估的初始文本、整合更改、提供校对标记，以及在动画过程中提供预览对象。

将协调器对象附加到你的视图上，通常是在创建和配置该视图时进行。提供一个采纳 [Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md) 协议、并能够访问你视图的文本内容和布局信息的委托对象。以下示例展示了一个自定义视图的扩展，它创建了协调器，并用视图本身对其进行初始化。这个自定义方法会在创建协调器对象并将其添加到视图之前，检查 Writing Tools 是否可用。

```swift
class MyTextView : UIView {
    var coordinator: UIWritingToolsCoordinator?

   //…
}

extension MyTextView : UIWritingToolsCoordinator.Delegate {

    func configureWritingTools() {
        guard UIWritingToolsCoordinator.isWritingToolsAvailable else { return }
        guard coordinator == nil else { return }
        
        coordinator = UIWritingToolsCoordinator(delegate:self)
        addInteraction(coordinator!)
    }
   //…
}
```

只要视图上存在协调器对象，就会让 UIKit 为该视图启用 Writing Tools 支持。当用户与你视图的上下文菜单交互时，UIKit 会自动向该菜单添加一条用于启动 Writing Tools 的命令。

要获取支持 Writing Tools 所需实现的委托方法完整列表，请参阅 [Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md)。

### 配置视图的 Writing Tools 行为

在为你的视图设置 Writing Tools 时，使用你支持的交互类型来配置协调器的 [preferredBehavior](uiwritingtoolscoordinator/preferredbehavior.md) 属性。Writing Tools 提供了不同层级的与视图内容的集成方式，这也会影响你为支持该功能需要做多少工作。使用完整体验时，你会向 UIKit 提供更多信息，以便它能直接在你的视图中做出更改。有限体验则将更多交互推给 Writing Tools UI，带来的集成度较低，但更容易实现。

在配置时，你还需要使用协调器的 [preferredResultOptions](uiwritingtoolscoordinator/preferredresultoptions.md) 属性指定视图所支持的文本内容类型。Writing Tools 用来评估你文本的模型可以生成纯文本或格式化文本。Writing Tools 默认支持所有类型的输出，但你可以根据需要将其限制为特定类型。

以下代码更新了前面的示例方法，并为协调器对象添加了一些偏好行为。除了希望 Writing Tools 交互采用行内体验之外，该方法还请求系统生成富文本以及可选的基于列表的内容。提供一个具体的结果选项列表，会告诉 Writing Tools 只生成该类型的内容。如果你的视图不支持某些特定类型的内容（比如表格），就可以提供这样的信息。

```swift
func configureWritingTools() {
    guard UIWritingToolsCoordinator.isWritingToolsAvailable else { return }
    guard coordinator == nil else { return }

    coordinator = UIWritingToolsCoordinator(delegate:self)
    coordinator?.preferredBehavior = .complete
    coordinator?.preferredResultOptions = [.richText, .list]
    addInteraction(coordinator!)
}
```

Writing Tools 的可用性取决于当前设备、其操作系统，以及它执行请求的就绪程度。在具备适当硬件的设备上，系统下载所需模型后，部分 Writing Tools 功能会在本地运行。不过，更复杂的请求需要网络连接，以便系统能使用 [Private Cloud Compute](https://security.apple.com/documentation/private-cloud-compute) 来评估提供的文本。

### 提供视图的文本以供评估

当用户在你的视图中启动 Writing Tools 时，系统会要求你的委托提供待评估的文本。根据用户想做的事情，Writing Tools 可能只请求已选中的文本，也可能请求你视图的全部文本。例如，用户可能只想校对当前选中的文本，也可能想校对视图中的全部文本。你需要在一个上下文对象中，从你的委托提供这段文本。

[Context](uiwritingtoolscoordinator/context.md) 对象是一个数据对象，你需要用请求的文本填充它。上下文对象为你和 Writing Tools 在整个单次操作过程中的通信提供了共同基础。对于每次请求，你需要为每个包含 Writing Tools 需要考虑的文本的文本存储对象，创建一个上下文对象。大多数视图只有一个文本存储对象，因此只会创建一个上下文对象。不过，如果某个视图使用多个子视图来管理其内容的不同部分，则可能会为每个子视图分配单独的文本存储对象。在这种情况下，你需要为每个包含所请求文本的子视图创建一个上下文对象。

为了请求你视图的上下文对象，协调器会调用你委托的 [- writingToolsCoordinator:requestsContextsForScope:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__requestscontextsfor_completion_).md>) 方法。使用该方法的参数来判断 Writing Tools 想要的是你视图的全部文本，还是仅仅其中一部分。以下示例创建了一个单独的上下文对象，其中包含当前选中的文本，或者视图的完整文本。创建上下文之后，这个自定义的 `storeContexts` 方法会保存对该上下文的引用，供后续任务使用。

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        requestsContextsFor scope: UIWritingToolsCoordinator.ContextScope,
        completion: @escaping ([UIWritingToolsCoordinator.Context]) -> Void) {

    // Store the created contexts for the completion handler.
    var contexts = [UIWritingToolsCoordinator.Context]()
                
    switch scope {
    case .userSelection:
        let context = getContextObjectForSelection()
        contexts.append(context)
        break
            
    case .fullDocument:
        let context = getContextObjectForFullDocument()
        contexts.append(context)
        break

    case .visibleArea:
        let context = getContextObjectForVisibleArea()
        contexts.append(context)
        break

    default:
        break
    }
        
    // Save references to the contexts for later delegate calls.
    storeContexts(contexts)
        
    // Deliver the contexts to Writing Tools.
    completion(contexts)
}
```

当只指定视图文本的一个子集时，请提供一些周围的文本，为 Writing Tools 的评估提供额外的内容。作为一般原则，应在上下文对象中包含完整的文本段落，而不仅仅是当前选中的文本。使用上下文对象的范围值来标识 Writing Tools 所请求的整体文本中的哪一部分。例如，如果你用当前选中的文本以及一些周围的文本填充一个上下文对象，就使用该上下文对象的 [range](uiwritingtoolscoordinator/context/range.md) 属性来指定所选文本在该对象中的位置。

创建上下文对象之后，缓存你需要的任何附加信息，以便将上下文对象中的文本映射到你视图文本存储中的文本。你需要知道每个上下文对象对应内容的起始位置，以便之后更新你的文本存储。一种方法是创建一个字典，将上下文对象的标识符映射到其文本在你文本存储中的起始位置。你可以使用这个值来调整 Writing Tools 之后提供给你的任何特定于上下文的范围。

以下示例展示了委托用来为当前文本选择创建上下文对象的方法。该方法调用了自定义的 `getSelectedTextToEvaluate` 函数，后者返回一个扩展版本的文本，其中既包含选中内容，也包含一些周围的文本。该方法还会返回这段扩展文本在视图文本存储中的起始位置。由于文本选择现在位于该文本的中间位置，该方法会用一个范围来初始化上下文对象，这个范围只提供选中文本相对于 `textToEvaluate` 起始位置的位置。该方法会将实际的起始位置保存在一个字典变量中，把这个值映射到上下文的唯一标识符。

```swift
var startingLocationsForContexts = [UUID : Int]()

func getContextObjectForSelection() -> UIWritingToolsCoordinator.Context {
    // Get the text to evaluate, which includes the text selection and some
    // of the surrounding text. The method returns (NSAttributedString, Int),
    // which represents the text itself, and the starting location of that
    // text in the view's text storage.
    let (textToEvaluate, startLocation) = getSelectedTextToEvaluate()

    // Get the NSRange for the text selection, relative to the text storage.
    let textSelectionRange = getTextSelectionRange()
    var contextRange = textSelectionRange
        
    // The view guarantees that startLocation is less than or equal to the
    // selection range. Adjust contextRange so that location 0 corresponds
    // to the first character in textToEvaluate. Keep the length the same.
    contextRange.location = textSelectionRange.location - startLocation
        
    // Create the new context object.
    let context = UIWritingToolsCoordinator.Context(attributedString: textToEvaluate, range: contextRange)
    
    // Save the starting location of the text, relative to the text storage.
    startingLocationsForContexts[context.identifier] = startLocation
    
    return context
}
```

创建上下文对象之后，你可以使用它的唯一标识符作为保存其他数据的键。你所创建的上下文对象，会在当前 Writing Tools 操作持续期间一直存在。如果用户拒绝了当前的更改并开始了一次新的操作，Writing Tools 会向你请求一组新的上下文对象。

### 将 Writing Tools 的更改整合到你的视图中

在评估完你视图的文本之后，Writing Tools 会将任何建议的更改传递给你的委托对象。如果你的视图采用了有限体验，Writing Tools 会等到用户接受了更改之后，才将其传递给你的视图。如果你采用了完整体验，Writing Tools 会在用户接受之前就传递这些更改。如果用户之后拒绝了这些更改，Writing Tools 会传递一组新的更改，将你视图的原始文本恢复回来。

在你委托的 [- writingToolsCoordinator:replaceRange:inContext:proposedText:reason:animationParameters:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__replace_in_proposedtext_reason_animationparameters_completion_).md>) 方法中，将指定的更改整合到你视图的文本存储中。Writing Tools 会针对它需要做出的每一处独立更改调用这个方法，而且可能会针对同一个上下文对象、用不同的范围值多次调用这个方法。以下这个简单的示例，会验证提供的范围信息，并验证视图自身为该上下文对象缓存的信息。如果一切都有效，该方法接着会计算出需要替换的正确文本范围，并创建一个事务来执行替换。在返回之前，该方法会用其整合的文本（如果有的话）执行提供的完成处理程序。

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        replace range: NSRange, 
        in context: UIWritingToolsCoordinator.Context, 
        proposedText replacementText: NSAttributedString, 
        reason: UIWritingToolsCoordinator.TextReplacementReason, 
        animationParameters: UIWritingToolsCoordinator.AnimationParameters?, 
        completion: @escaping (NSAttributedString?) -> Void) {
        
    // Make sure there's a valid starting location in the text storage.
    guard let startingLocation = startingLocationsForContexts[context.identifier] 
        else { completion(nil); return }
    guard let textStorage = textContentStorage.textStorage else { completion(nil); return }

    // Determine the correct location in the text storage.
    let adjustedRange = NSRange(location: startingLocation + range.location, length: range.length)
        
    // Update the view’s NSTextContentManager using a transaction.
    textContentStorage.performEditingTransaction {
        textStorage.replaceCharacters(in: adjustedRange, with: replacementText)
    }
    
    completion(replacementText)
}
```

每次替换操作之后，根据需要更新你 App 的其他部分，以反映这一更改。当你使用事务进行更改时，[NSTextContentManager](nstextcontentmanager.md) 对象会自动生成所需的布局更新。如果你需要更新界面的其他部分，请从你的 [- writingToolsCoordinator:replaceRange:inContext:proposedText:reason:animationParameters:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__replace_in_proposedtext_reason_animationparameters_completion_).md>) 方法发起这些更改。例如，你可能需要更新一个显示文稿当前字符数的视图。检查 `reason` 参数，以判断 Writing Tools 何时是以交互方式进行更改，并使用提供的动画参数对象来创建实际的动画。

### 更新视图的选中文本

在处理你视图的选中文本时，Writing Tools 会更新文本选择，以反映任何文本更新。使用你委托的 [- writingToolsCoordinator:selectRanges:inContext:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__select_in_completion_).md>) 方法来更新视图中的选中文本。该方法会传递一个范围值数组，以便视图能够创建不连续的选择。如果你的视图只支持一段连续的选中字符范围，请根据 `ranges` 数组中的第一个元素来更新视图的选择。

在实现你的委托方法时，请记得根据上下文对象中文本起始位置的偏移量来调整范围值。以下示例通过加上在操作开始时为该上下文对象记录的起始位置，创建了一组调整后的范围。然后它将这些信息传递给视图的文本引擎，以高亮显示相应范围的文本。

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        select ranges: [NSValue], 
        in context: UIWritingToolsCoordinator.Context, 
        completion: @escaping () -> Void) {
        
    guard let startingLocation = startingLocationsForContexts[context.identifier] 
              else { completion(); return }
    var adjustedRanges = [NSRange]()
        
    for value in ranges {
        let range = value.rangeValue
        let newRange = NSRange(location: startingLocation + range.location, length: range.length)
        adjustedRanges.append(newRange)
    }

    // Highlight the specified text in the view.
    selectTextInDocument(adjustedRanges)
    completion()
}
```

### 为行内动画更改生成预览图像

当你为视图选择完整的 Writing Tools 体验时，系统会直接在你的视图中为内容更改制作动画。系统会在 Writing Tools 开始评估你的文本时、在它移除旧文本时，以及在它插入新文本时创建动画。由于这些动画涉及你的内容，你必须协助系统创建它们。在适当的时机，协调器会要求你的委托对象执行以下任务：

1. 为你内容的特定部分创建一张预览图像。
2. 在动画开始时隐藏该内容。
3. 在动画结束时再次显示该内容。

要为你的文本创建预览图像，请在你委托的 [- writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__requestspreviewfor_of_in_completion_).md>) 方法中，使用你的布局管理器和 [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) 来生成图像。使用你的布局管理器获取包围指定文本的框架矩形，并用该矩形的大小配置你的图像渲染器。在你的渲染代码中，配置一条裁剪路径，将绘制限制在仅包含指定文本的区域内，并将该文本渲染到一个透明背景上。

以下示例展示了 [- writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__requestspreviewfor_of_in_completion_).md>) 方法的一种实现，它会为视图的文本创建一张预览图像。该方法依赖视图的布局管理器，来获取包围指定范围内每一行文本的文本矩形。它还使用布局管理器在图形渲染器的代码块中绘制文本。图像渲染器会生成一张带有渲染文本的图像，该方法将其放入一个图像视图中，并用它创建一个 [UITargetedPreview](uitargetedpreview.md) 对象。设置图像视图的框架矩形，会告诉 Writing Tools 应该把这张图像放置在整个文本视图中的哪个位置。在创建动画时，Writing Tools 会将所需的视觉效果应用到提供的图像视图上，而不是文本本身。

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        requestsPreviewFor textAnimation: UIWritingToolsCoordinator.TextAnimation, 
        of range: NSRange, 
        in context: UIWritingToolsCoordinator.Context, 
        completion: @escaping (UITargetedPreview?) -> Void) {
        
    let textRange = MyTextRange(range)         // Create the view's custom subclass of NSTextRange.
    let textRects = getTextRectangles(range)   // Returns an array of NSValue<NSRect*>.

    if !textRange.isEmpty {
        // Get the frame rectangle that encloses the text.
        let textFrame = unionRect(for: textRects.map({$0.cgRectValue}))
            
        // Create the image renderer and render the image.
        let renderer = UIGraphicsImageRenderer(bounds: textFrame)
        let image = renderer.image { context in
            // Limit drawing to the text rectangles.
            context.cgContext.clip(to: textRects.map({$0.cgRectValue}))
                
            // Draw the specified range of text using the view's layout manager.
            drawTextInRange(range)
        }
        // Create an image view and set its frame to match the area with the text.
        let imageView = UIImageView(image:image)
        imageView.frame = textFrame
            
        // Create the targeted preview.
        let parameters = UIPreviewParameters(textLineRects: 
                       textRects.map({NSValue(cgRect: $0.cgRectValue)}))
        let target = UIPreviewTarget(container: self, center: self.center)
        let preview = UITargetedPreview(view: imageView, parameters: parameters, target: target)
            
        completion(preview)
    }
    else {
        completion(nil)
    }
}
```

除了提供初始图像之外，还要使用 [- writingToolsCoordinator:prepareForTextAnimation:forRange:inContext:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__preparefor_for_in_completion_).md>) 方法来隐藏你视图中指定范围的文本。UIKit 会将你 [UITargetedPreview](uitargetedpreview.md) 对象中的图像视图，插入到你视图中包含隐藏文本的同一部分。图像视图的放置位置非常重要，这也是为什么你必须将其框架矩形设置为文本在你视图中的精确位置。动画结束后，Writing Tools 会调用 [- writingToolsCoordinator:finishTextAnimation:forRange:inContext:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__finish_for_in_completion_).md>) 方法，以便你再次显示指定范围内的文本。

### 为你的内容创建校对标记

如果用户选择了某个校对选项，Writing Tools 会评估你视图的文本，并要求你提供用于装饰该视图的校对标记。对于每个标记，Writing Tools 都要求你提供一条贝塞尔路径，为特定范围内的文本添加下划线。以下示例使用视图的布局管理器，获取指定文本范围的边界矩形。然后它将这些矩形展平，在文本下方创建一个线条形状，并将得到的路径传递给完成处理程序。这段代码为每个矩形创建单独的形状，以应对校对标记跨越多行文本的情况。

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        requestsUnderlinePathsFor range: NSRange, 
        in context: UIWritingToolsCoordinator.Context, 
        completion: @escaping ([UIBezierPath]) -> Void) {

    let textRects = getTextRectangles(range)   // Returns an array of NSValue<NSRect*>.
        
    var paths = [UIBezierPath]()
    for rect in textRects.map({$0.cgRectValue}) {
        let underlineHeight: CGFloat = 2
        let newRect = CGRect(x: rect.origin.x, y: rect.origin.y + rect.height - (underlineHeight/2), 
                             width: rect.width, height: underlineHeight)
        paths.append(UIBezierPath(rect: newRect))
    }
                
    completion(paths)

}
```

除了提供校对标记的形状之外，Writing Tools 还会要求你提供文本本身的边界矩形。Writing Tools 使用这些边界矩形在你的文本周围绘制高亮。以下示例获取指定文本范围的边界矩形，并为每个矩形传递一条贝塞尔路径给完成处理程序：

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        requestsBoundingBezierPathsFor range: NSRange, 
        in context: UIWritingToolsCoordinator.Context, 
        completion: @escaping ([UIBezierPath]) -> Void) {

    let textRects = getTextRectangles(range)   // Returns an array of NSValue<NSRect*>.
        
    var paths = [UIBezierPath]()
    for rect in textRects.map({$0.cgRectValue}) {
        paths.append(UIBezierPath(rect: rect))
    }
                
    completion(paths)
}
```

### 响应状态变化

在内容变更的过程中，Writing Tools 系统的状态会根据当前发生的情况而变化。Writing Tools 从非活跃状态开始，但会根据它所创建的体验类型迅速转移到其他状态。当用户接受或拒绝当前操作的更改时，Writing Tools 会转回非活跃状态。你可以使用委托的 [- writingToolsCoordinator:willChangeToState:completion:](<uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(__willchangeto_completion_).md>) 方法来响应以下几类变化：

- 使用转换到 [UIWritingToolsCoordinatorStateInactive](uiwritingtoolscoordinator/state-swift.enum/inactive.md) 状态的时机，清除上一次操作留下的任何缓存数据。
- 使用转换到 [UIWritingToolsCoordinatorStateNoninteractive](uiwritingtoolscoordinator/state-swift.enum/noninteractive.md) 或 [UIWritingToolsCoordinatorStateInteractiveResting](uiwritingtoolscoordinator/state-swift.enum/interactiveresting.md) 状态的时机，来判断与你视图的交互程度。
- 使用转换到 [UIWritingToolsCoordinatorStateInteractiveStreaming](uiwritingtoolscoordinator/state-swift.enum/interactivestreaming.md) 状态的时机，启动进度控制，或以其他方式表明 Writing Tools 正在处理该请求。此外，使用进入和离开这个状态的转换来实现撤销合并（undo coalescing）。具体来说，在转换到这个状态时开启一个新的撤销组，并在离开这个状态时结束该撤销组。通过调用 [- updateRange:withText:reason:forContextWithIdentifier:](<uiwritingtoolscoordinator/updaterange(__with_reason_forcontextwithidentifier_).md>) 方法，将任何撤销栈的更改通知给 Writing Tools。

要了解如何处理各个具体状态的更多信息，请参阅 [State](uiwritingtoolscoordinator/state-swift.enum.md) 类型。

### 将内容的外部更改告知协调器

当 Writing Tools 处于活跃状态时，它会跟踪你视图中文本的更改。如果你在 Writing Tools 处于活跃状态期间更改了视图的文本存储，请立即让系统知晓这一点。Writing Tools 会在内部跟踪它自己所做的更改，因此它需要知道任何外部更改，以确保向你的委托对象传递准确的信息。要将任何更改通知给 Writing Tools，请使用以下方法之一：

- 如果你更改的文本对应于某个上下文对象中的文本，请调用 [- updateRange:withText:reason:forContextWithIdentifier:](<uiwritingtoolscoordinator/updaterange(__with_reason_forcontextwithidentifier_).md>) 方法。根据你所做更改的范围，Writing Tools 可能会整合你的更改，也可能直接中止当前操作。
- 调用 [- updateForReflowedTextInContextWithIdentifier:](<uiwritingtoolscoordinator/updateforreflowedtextincontextwithidentifier(__).md>) 方法，报告任何影响你视图布局的更改。例如，如果你视图的大小发生了变化，或者你更改了某个上下文对象内容之前的文本，就应该调用这个方法。当你调用这个方法时，Writing Tools 会请求新的预览、校对标记以及其他依赖布局的信息。

## 另请参阅

### Writing Tools for custom views

- [UIWritingToolsCoordinator](uiwritingtoolscoordinator.md) — 一个管理 Writing Tools 与你自定义文本视图之间交互的对象。
- [Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md) — 一个用于管理 Writing Tools 与你自定义文本视图之间交互的接口。
- [Context](uiwritingtoolscoordinator/context.md) — 一个用于与 Writing Tools 共享你自定义视图文本的数据对象。
- [AnimationParameters](uiwritingtoolscoordinator/animationparameters.md) — 一个用于配置随 Writing Tools 动画一起运行的附加任务或动画的对象。
</content>
