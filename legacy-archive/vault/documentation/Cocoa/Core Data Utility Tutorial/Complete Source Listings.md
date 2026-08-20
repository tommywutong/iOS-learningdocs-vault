---
title: Core Data 实用工具教程
apple_id: TP40001800
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataUtilityTutorial/Articles/08_sourceListings.html
archived_at: '2026-07-15T07:14:28.975561Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 实用工具教程](Introduction%20to%20Core%20Data%20Utility%20Tutorial.md)


[下一页](Document%20Revision%20History.md)[上一页](Listing%20Previous%20Runs.md)

# 完整源代码清单

完成后的教程中，`main` 源文件的完整清单如清单 7-1 所示。

__清单 7-1__  main 源文件的完整清单

```objc
Complete listing of the main source file

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>


#import "Run.h"

NSManagedObjectModel *managedObjectModel();
NSManagedObjectContext *managedObjectContext();
NSURL *applicationLogDirectory();

NSString *STORE_TYPE;
NSString *STORE_FILENAME;
NSString *SUPPORT_DIRECTORY;


int main (int argc, const char * argv[])
{
    @autoreleasepool {

        STORE_TYPE = NSXMLStoreType;
        STORE_FILENAME = @"CDCLI.cdcli";
        SUPPORT_DIRECTORY = @"CDCLI";

        NSManagedObjectModel *mom = managedObjectModel();
        NSLog(@"mom: %@", mom);

        if (applicationLogDirectory() == nil) {
            NSLog(@"Could not find application support directory\nExiting...");
            exit(1);
        }

        NSManagedObjectContext *moc = managedObjectContext();

        NSEntityDescription *runEntity = [[mom entitiesByName] objectForKey:@"Run"];
        Run *run = [[Run alloc] initWithEntity:runEntity
                insertIntoManagedObjectContext:moc];

        NSProcessInfo *processInfo = [NSProcessInfo processInfo];
        run.processID = [processInfo processIdentifier];

        NSLog(@"run.processID: %ld", run.processID);


        NSError *error;

        if (![managedObjectContext() save: &error]) {
            NSLog(@"Error while saving\n%@",
                  ([error localizedDescription] != nil) ? [error localizedDescription] : @"Unknown Error");
            exit(1);
        }



        NSFetchRequest *request = [NSFetchRequest fetchRequestWithEntityName:@"Run"];

        NSSortDescriptor *sortDescriptor = [[NSSortDescriptor alloc]
                                            initWithKey:@"date" ascending:YES];

        [request setSortDescriptors:@[sortDescriptor]];

        error = nil;
        NSArray *fetchedArray = [moc executeFetchRequest:request error:&error];

        if (fetchedArray == nil) {
            NSLog(@"Error while fetching\n%@",
                  ([error localizedDescription] != nil) ? [error localizedDescription] : @"Unknown Error");
            exit(1);
        }

        NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
        [formatter setDateStyle:NSDateFormatterMediumStyle];
        [formatter setTimeStyle:NSDateFormatterMediumStyle];

        NSLog(@"%@ run history:", [processInfo processName]);

        for (Run *aRun in fetchedArray) {
            NSLog(@"On %@ as process ID %ld", [formatter stringForObjectValue:aRun.date], aRun.processID);
        }

    }
    return 0;
}



NSManagedObjectModel *managedObjectModel() {

    static NSManagedObjectModel *mom = nil;

    if (mom != nil) {
        return mom;
    }

    NSEntityDescription *runEntity = [[NSEntityDescription alloc] init];
    [runEntity setName:@"Run"];
    [runEntity setManagedObjectClassName:@"Run"];

    NSAttributeDescription *dateAttribute = [[NSAttributeDescription alloc] init];

    [dateAttribute setName:@"date"];
    [dateAttribute setAttributeType:NSDateAttributeType];
    [dateAttribute setOptional:NO];


    NSAttributeDescription *idAttribute = [[NSAttributeDescription alloc] init];

    [idAttribute setName:@"processID"];
    [idAttribute setAttributeType:NSInteger64AttributeType];
    [idAttribute setOptional:NO];
    [idAttribute setDefaultValue:@(-1)];

    NSExpression *lhs = [NSExpression expressionForEvaluatedObject];
    NSExpression *rhs = [NSExpression expressionForConstantValue:@0];

    NSPredicate *validationPredicate = [NSComparisonPredicate
                                            predicateWithLeftExpression:lhs
                                            rightExpression:rhs
                                            modifier:NSDirectPredicateModifier
                                            type:NSGreaterThanPredicateOperatorType
                                            options:0];

    NSString *validationWarning = @"Process ID < 1";

    [idAttribute setValidationPredicates:@[validationPredicate]
                 withValidationWarnings:@[validationWarning]];

    [runEntity setProperties:@[dateAttribute, idAttribute]];

    mom = [[NSManagedObjectModel alloc] init];
    [mom setEntities:@[runEntity]];

    NSDictionary *localizationDictionary = @{
                            @"Property/date/Entity/Run":@"Date",
                            @"Property/processID/Entity/Run":@"Process ID",
                            @"ErrorString/Process ID < 1":@"Process ID must not be less than 1"};

    [mom setLocalizationDictionary:localizationDictionary];

    return mom;
}



NSManagedObjectContext *managedObjectContext()
{
    static NSManagedObjectContext *moc = nil;

    if (moc != nil) {
        return moc;
    }

    NSPersistentStoreCoordinator *coordinator =
        [[NSPersistentStoreCoordinator alloc]
            initWithManagedObjectModel: managedObjectModel()];

    NSString *STORE_TYPE = NSXMLStoreType;
    NSString *STORE_FILENAME = @"CDCLI.cdcli";

    NSError *error;
    NSURL *url = [applicationLogDirectory() URLByAppendingPathComponent:STORE_FILENAME];

    NSPersistentStore *newStore = [coordinator addPersistentStoreWithType:STORE_TYPE
                                               configuration:nil URL:url options:nil
                                               error:&error];

    if (newStore == nil) {
        NSLog(@"Store Configuration Failure\n%@",
              ([error localizedDescription] != nil) ?
              [error localizedDescription] : @"Unknown Error");
    }


    moc = [[NSManagedObjectContext alloc] initWithConcurrencyType:NSMainQueueConcurrencyType];
    [moc setPersistentStoreCoordinator:coordinator];

    return moc;
}



NSURL *applicationLogDirectory() {

    NSString *LOG_DIRECTORY = @"CDCLI";
    static NSURL *ald = nil;

    if (ald == nil) {

        NSFileManager *fileManager = [[NSFileManager alloc] init];
        NSError *error;
        NSURL *libraryURL = [fileManager URLForDirectory:NSLibraryDirectory inDomain:NSUserDomainMask appropriateForURL:nil create:YES error:&error];
        if (libraryURL == nil) {
            NSLog(@"Could not access Library directory\n%@", [error localizedDescription]);
        }
        else {
            ald = [libraryURL URLByAppendingPathComponent:@"Logs"];
            ald = [ald URLByAppendingPathComponent:LOG_DIRECTORY];
            NSDictionary *properties = [ald resourceValuesForKeys:@[NSURLIsDirectoryKey]
                                                            error:&error];
            if (properties == nil) {
                if (![fileManager createDirectoryAtURL:ald withIntermediateDirectories:YES attributes:nil error:&error]) {
                    NSLog(@"Could not create directory %@\n%@", [ald path], [error localizedDescription]);
                    ald = nil;
                }
            }
        }
    }
    return ald;
}
```


完成后的教程中，Run 类的声明和实现的完整清单分别如清单 7-2 和清单 7-3 所示。

__清单 7-2__  Run 类声明的代码清单

```objc
#import <CoreData/CoreData.h>


@interface Run : NSManagedObject

@property (strong) NSDate *date;
@property (assign) NSInteger processID;

@end
```


__清单 7-3__  Run 类实现的代码清单

```objc
#import "Run.h"

@interface Run ()
@property (strong) NSDate *primitiveDate;
@end

@implementation Run

@dynamic date, primitiveDate, processID;


- (void)awakeFromInsert
{
    [super awakeFromInsert];
    self.primitiveDate = [NSDate date];
}

- (void)setNilValueForKey:(NSString *)key
{
    if ([key isEqualToString:@"processID"]) {
        self.processID = 0;
    }
    else {
        [super setNilValueForKey:key];
    }
}

@end
```

[下一页](Document%20Revision%20History.md)[上一页](Listing%20Previous%20Runs.md)

