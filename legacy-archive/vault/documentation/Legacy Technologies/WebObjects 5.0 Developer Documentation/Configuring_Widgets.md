---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToJavaClient/Tutorial/Configuring_Widgets.html
archived_at: '2026-07-15T08:12:21.000089Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Configuring_Properties.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Typical_Workflow.md)

## Configuring Widgets

The Assistant's Widgets tab allows you to configure the
widgets used to display and manipulate properties (attributes and
relationships). For example, you can change the widget that's
used to display a particular attribute, and you can set the widget's
resizing behavior.

1. Change the
   widget for the PlotSummary entity's `summary` attribute
   to a text area.

   Click the Widget tab in the Assistant. Choose
   form from the Task pull-down list, PlotSummary from the Entity pull-down
   list, and `summary` from
   the Property pull-down list.

|  |
| --- |
| __WARNING__ |
| Don't use Movie as the Entity and `plotSummary` as the property key. You're configuring the widget used to display the `summary` property of the PlotSummary entity, not the widget for displaying the `plotSummary` relationship of the Movie entity. So be sure the Entity pull-down list is set to PlotSummary and the Property pull-down list is set to `summary`. |

   Set the Widget Type to EOTextAreaController. Save the change,
   and open a new Movie form window to see the result.
2. Remove the Summary label.

   The `summary` Widget
   label is redundant with the PlotSummary tab label, so you should remove
   it.

   If you opened a new Movie form window to see the
   change you made in step 1, you first need to restore the Assistant's
   Widget tab settings. Set the Task to form, the Entity to PlotSummary,
   and the Property to `summary`.

   Now
   set the `summary` property's
   "Show Label Component" setting to `False`.
   Save the change, and open a new form to see it.
3. Set sizing information for the `summary` widget.

   Resize
   the window so it's much larger than the default size. Notice that
   the `summary` widget doesn't
   resize vertically. To prevent the waste of screen real estate and
   to display more of the summary upon window resizing, you need to
   set the widget to resize.

   Restore the Assistant Task,
   Entity, and Property settings to form, PlotSummary, and `summary`,
   respectively. Now set the `summary` property's
   "Vertically Resizable" setting to `True`.
   Save the change, and open a new form to see it.
4. Change the widget for the Review entity's `review` attribute
   to a text area.

   In the Widget tab of the Assistant, set the
   Task to `form`, Entity
   to Review, and Property to `review`.
   Set the Widget Type to EOTextAreaController. Save the change.
5. Set sizing information for the `review` widget.

   In
   a new Movie form window, click the Reviews tab. Resize the window
   so it's much larger than the default size. Notice that the Review
   widget doesn't resize vertically. In this window, this behavior
   is appropriate because the table above the Review widget does resize
   to take up the added area.

   However, you might want a
   larger area in which to display movie reviews. If you set the text
   area to resize vertically, the widget still doesn't resize because
   the table view above it does. So to provide a larger text area,
   you can set a minimum height.

   Restore the Assistant
   Task, Entity, and Property settings to `form`,
   Review, and `review`, respectively.
   Now set the `review` property's `Minimum
   Height` to `200`.
   Save the change, and open a new form to see it.

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Configuring_Properties.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Typical_Workflow.md)

© 2001 Apple Computer, Inc.
