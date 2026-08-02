---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/Person.html
archived_at: '2026-07-15T07:48:24.966697Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](CustomClasses.md)

## Implement Person

- Choose File ! New in Project to add another class.
- Type __Person.java__ as the name of the class.
- Deselect the Create header option.
- Click OK.
!- Declare Person. Give it a single instance variable, __personRecord__, which contains information about the person. Write a constructor to initialize the variable.

```
    import next.util.*;
    import next.wo.*;

    public class Person extends Object {
        ImmutableHashtable personRecord;

        public Person(ImmutableHashtable personDict) {
            super();
            personRecord = personDict;
        }
    }
```


Person initializes the __personRecord__ instance variable using a dictionary returned by the Main component of the Registration application.

- Write a method that validates the information in __personRecord__:

```
    public ImmutableHashtable validate() {
        MutableHashtable valid = new MutableHashtable();

        if ((((String)(personRecord.get("address"))).length() == 0) &&
            (((String)(personRecord.get("name"))).length() == 0)) {
            valid.put("failureReason",
                "You must supply a name and address");
            valid.put("valid", "No");
        } else if (((String)(personRecord.get("name"))).length()
            == 0) {
            valid.put("failureReason", "You must supply a name.");
            valid.put("valid", "No");
        } else if (((String)(personRecord.get("address"))).length()
            == 0) {
            valid.put("failureReason",
                "You must supply an address");
            valid.put("valid", "No");
        } else {
            valid.put("valid", "Yes");
        }
        return valid;
    }
```


Person's __validate__ method checks whether the data entered by the user includes values for a name and address. The __validate__ method returns a dictionary. This dictionary contains a status message and a validation flag that indicates whether the registration should be allowed to proceed. If the user failed to enter a name or address, the validation flag value is "No," which disallows the registration. The status message then prompts the user to supply the missing information.

- Implement two more methods as shown below:

```
    public String name() {
        return (String)(personRecord.get("name"));
    }

    public ImmutableHashtable personAsDictionary() {
         return personRecord;
    }
```


The __name__ method is simply used to return the Person's name, while the method __personAsDictionary__ returns a dictionary representation of the Person. The dictionary representation is used when the Person's data is written out to a file in a property list format (in RegistrationManager's __writeRegistrantsToFile__ method).

[!Table of Contents](compiled.book.md) [!Next Section](Application.md)
