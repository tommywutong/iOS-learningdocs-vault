---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/ImplementingSAD.html
archived_at: '2026-07-15T07:46:35.169487Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](MakingOwn0.md)

# __Implementing the SimpleAssociationDestination Interface__

If you write an applet, or aquire the source code for an applet, you will probably want to follow this procedure to give the applet the associative behavior it needs to be a client-side component.

1. In the class declaration, insert the "implements SimpleAssociationDestination" clause.

   ```
      public class MyApplet extends Applet implements SimpleAssociationDestination {
         // ....
       }
   ```
2. Implement the __keys()__ method to return a list (Vector) of state keys managed by the applet.

   ```
      public Vector keys() {
           Vector keys = new Vector(1);
           keys.addElement("title");
           return keys;
       }
   ```
3. Implement the __takeValueForKey(__Object, String__)__ and __valueForKey(__String__)__ methods to set and get the values of keys.

   ```
       synchronized public Object valueForKey(String key) {
           if (key.equals("title")) {
               return this.getLabel();
           }
       }

       synchronized public void takeValueForKey(Object value, String key) {
           if (key.equals("title")) {
               if ((value != null) && !(value instanceof String)) {
                   System.out.println("Object value of wrong type set for key
                           'title'.  Value must be a String.");
               } else {
                   self.setLabel(((value == null) ? "" : (String)value));
               }
       }
   ```

   You should be able to access the keys directly or, ideally, through accessor methods ("getLabel()" and "setLabel()" in the above example). It is a good idea to use the __synchronize__ modifier with __takeValueForKey(__Object, String__)__ and __valueForKey(__String__)__ because these methods can be invoked from other threads to read or set data.

   The remaining steps apply only if the applet has an action.
4. Declare an instance variable for the applet's Association object and then, in __setAssociation(__Association__)__, assigned the passed-in object to that variable.

   ```
       protected Association _assoc;
       // ...
       synchronized public void setAssociation(Association assoc) {
           _assoc = assoc;
       }
   ```

   The Association object must be stored so it can be used later as the receiver of the __invokeAction()__ message. The Association forwards the action to the AppletGroupController, which handles the invocation of the server-side action method.
5. When an action is invoked in the applet, send __invokeAction(__String__)__ to the applet's Association.

   ```
       synchronized public boolean action(Event evt, Object what) {
           if (_assoc != null) {
               _assoc.invokeAction("action");
           }
           return true;
       }
   ```

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](AssocSubclass.md)
