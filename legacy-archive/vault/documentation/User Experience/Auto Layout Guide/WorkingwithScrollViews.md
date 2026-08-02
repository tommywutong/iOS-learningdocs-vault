---
title: Auto Layout Guide
apple_id: TP40010853
resource_type: Guide
platform: tvOS|iOS|macOS
topic: User Experience
technology: AppKit
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/WorkingwithScrollViews.html
archived_at: '2026-07-18T02:10:52.784078Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Auto Layout Guide](index.md)



## Working with Scroll Views

When working with scroll views, you need to define both the size and position of the scroll view’s frame within its superview, and the size of the scroll view’s content area. All of these features can be set using Auto Layout.

To support scroll views, the system interprets constraints differently, depending on where the constraints are located.

- Any constraints between the scroll view and objects outside the scroll view attach to the scroll view’s frame, just as with any other view.
- For constraints between the scroll view and its content, the behavior varies depending on the attributes being constrained:

  - Constraints between the edges or margins of the scroll view and its content attach to the scroll view’s content area.
  - Constraints between the height, width, or centers attach to the scroll view’s frame.
- You can also use constraints between the scroll view’s content and objects outside the scroll view to provide a fixed position for the scroll view’s content, making that content appear to float over the scroll view.

For most common layout tasks, the logic becomes far easier if you use a dummy view or layout group to contain the scroll view’s content. When working in Interface Builder, the general approach is shown below:

1. Add the scroll view to the scene.
2. Draw constraints to define the scroll view’s size and position, as normal.
3. Add a view to the scroll view. Set the view’s Xcode specific label to Content View.
4. Pin the content view’s top, bottom, leading, and trailing edges to the scroll view’s corresponding edges. The content view now defines the scroll view’s content area.

   > [!NOTE]
   > 
5. (Optional) To disable horizontal scrolling, set the content view’s width equal to the scroll view’s width. The content view now fills the scroll view horizontally.
6. (Optional) To disable vertical scrolling, set the content view’s height equal to the scroll view’s height. The content view now fills the scroll view horizontally.
7. Lay out the scroll view’s content inside the content view. Use constraints to position the content inside the content view as normal.

   > [!NOTE]
   > 

[Size-Class-Specific Layout](Size-ClassSpecificLayout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrwfvjvomi)

[Working with Self-Sizing Table View Cells](WorkingwithSelf-SizingTableViewCells.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqnjtfvbuqmrvfvjvomi)
