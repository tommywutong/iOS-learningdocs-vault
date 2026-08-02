---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/AssocSubclass.html
archived_at: '2026-07-15T07:46:34.168302Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](ImplementingSAD.md)

# __Creating a Subclass of Association__

If you have an applet, but do not have the source code for it, you must follow the following strategy for making the applet a client-side component. You must know the applet's accessor methods for setting and getting state, and, if the applet triggers actions, there must be some way for your Association to detect this. _If the applet doesn't have API for getting and setting state, you cannot make the applet into a client-side component_.

1. Declare an subclass of the Association class.

   ```
       class MyAssociation extends Association {
           // ...
       }
   ```
2. Implement the __keys()__ method to return a list (Vector) of keys managed by the applet. See "[Implementing the SimpleAssociationDestination Interface](ImplementingSAD.md#apple-kjcumnzqguytm)" for an example.
3. Implement the __takeValueForKey(__Object, String__)__ and __valueForKey(__String__)__ methods to set and get the values of keys. Use Association's __destination()__ method to obtain the destination object (that is, the applet).

   ```
       synchronized public Object valueForKey(String key) {
           Object dest = this.destination();
           if (key.equals("title")) {
               return ((MyApplet)dest).getLabel();
           }
       }

       synchronized public void takeValueForKey(Object value, String key) {
           Object dest = this.destination();
           if (key.equals("title")) {

               if ((value != null) && !(value instanceof String)) {
                   System.out.println("Object value of wrong type set for key
                           'title'.  Value must be a String.");
               } else {
                   ((MyApplet)dest).setLabel(((value == null) ? "" : (String)value));
               }
       }
   ```

   Note that the class of the destination applet ("MyApplet" in the example) must be cast.

   If the applet triggers an action method, it must some mechanism for communicating this event to observers (such as an "observeGadget()" method).
4. The Association responds to the triggering of the applet's action by sending __invokeAction(__String__)__ to itself.

   ```
       public void observeGadget(Object sender, String action) { // fictictious
           if ((sender instanceof Gadget) && action.equals("vacuum")) {
               this.invokeAction(action);
           }
       }
   ```

   Note that in this hypothetical example, the Association must first set itself up as an observer.
