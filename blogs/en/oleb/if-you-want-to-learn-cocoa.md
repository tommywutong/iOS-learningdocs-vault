---
title: If You Want to Learn Cocoa...
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/03/if-you-want-to-learn-cocoa/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5036f81741b49dd9'
translated: false
---

> 原文：[If You Want to Learn Cocoa...](https://oleb.net/blog/2010/03/if-you-want-to-learn-cocoa/)　·　Ole Begemann

# If You Want to Learn Cocoa...

…be prepared to write a lot more code than in your typical “scripting” language. Three examples (I am using Ruby for comparison because it is the scripting language I am most familiar with; things would look very much the same with Python or PHP):

# 1. Declare a small hash/dictionary of key-value pairs

## Ruby:

```
person = {
  :name => "John Appleseed",
  :age => 30,
  :favorite_fruit => [ "apple", "banana", "kiwi" ]
}
```

## Cocoa:

```
NSDictionary *person = [NSDictionary dictionaryWithObjectsAndKeys:
                        @"John Appleseed", @"name",
                        [NSNumber numberWithInteger:30], @"age",
                        [NSArray arrayWithObjects:@"apple", @"banana", @"kiwi", nil], @"favoriteFruit",
                        nil];
```

Now which of these is easier to read?

# 2. What day of the month is today?

## Ruby:

```
today = Date.today                       # => #
puts "Day of the month: %d" % today.day  # => Day of the month: 7
```

## Cocoa:

```
NSDate *today = [NSDate date];                        // => 2010-03-07 15:15:26 +0100
NSCalendar *calendar = [NSCalendar currentCalendar];  // => <__NSCFCalendar: 0x100400160>
NSDateComponents *components = [calendar components:NSDayCalendarUnit
                                           fromDate:today];
NSLog(@"Day of the month: %d", [components day]);     // => Day of the month: 7
```

# 3. Fetch something from the data store

## Ruby on Rails (Active Record):

```
result = Person.find(:all, :conditions => { :first_name => "John" }, :order => "created_at DESC")
```

## Cocoa (Core Data):

```
NSFetchRequest *fetchRequest = [[NSFetchRequest alloc] init];

NSEntityDescription *entity = [NSEntityDescription entityForName:@"Person" inManagedObjectContext:self.managedObjectContext];
[fetchRequest setEntity:entity];

NSPredicate *predicate = [NSPredicate predicateWithFormat:@"firstName == %@", @"John"];
[fetchRequest setPredicate:predicate];

NSSortDescriptor *sortDescriptor = [[NSSortDescriptor alloc] initWithKey:@"creationDate" ascending:NO];
[fetchRequest setSortDescriptors:[NSArray arrayWithObject:sortDescriptor]];
[sortDescriptor release];

NSError *fetchError = nil;
NSArray *fetchResult = [self.managedObjectContext executeFetchRequest:fetchRequest error:&error];
[fetchRequest release];
```

Now I know this is not a fair comparison, Objective-C/Cocoa has many advantages over Ruby et al., you can’t compare Core Data to Active Record, etc. Still, I find the differences very striking, especially regarding the readability of the code.
