---
title: 'PIVToken: Using CryptoTokenKit to add support for new types of tokens'
apple_id: TP40017285
resource_type: Sample Code
platform: macOS
topic: null
technology: CryptoTokenKit
published: '2016-09-22'
source_url: https://developer.apple.com/library/archive/samplecode/PIVToken/Listings/PIVToken_Token_m.html
archived_at: '2026-07-18T03:18:35.416720Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PIVToken: Using CryptoTokenKit to add support for new types of tokens](PIVToken-%20Using%20CryptoTokenKit%20to%20add%20support%20for%20new%20types%20of%20tokens.md)


[Next](PIVToken-TokenDriver.m.md)[Previous](PIVToken-NSDataZip.m.md)

# PIVToken/Token.m

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements PIV token core
 */

#import <os/log.h>
#import <Foundation/Foundation.h>
#import <CryptoTokenKit/CryptoTokenKit.h>

#import "Token.h"
#import "NSData_Zip.h"

@implementation NSData(hexString)

- (NSString *)hexString {

    NSUInteger capacity = self.length * 2;
    NSMutableString *stringBuffer = [NSMutableString stringWithCapacity:capacity];
    const unsigned char *dataBuffer = self.bytes;

    for (NSInteger i = 0; i < self.length; i++) {
        [stringBuffer appendFormat:@"%02lX", (unsigned long)dataBuffer[i]];
    }

    return stringBuffer;
}

@end

@implementation PIVTokenKeychainKey

- (instancetype)initWithCertificate:(SecCertificateRef)certificateRef objectID:(TKTokenObjectID)objectID certificateID:(TKTokenObjectID)certificateID alwaysAuthenticate:(BOOL)alwaysAuthenticate {
    if (self = [super initWithCertificate:certificateRef objectID:objectID]) {
        _certificateID = certificateID;
        _alwaysAuthenticate = alwaysAuthenticate;
    }
    return self;
}

- (UInt8)keyID {
    return [self.objectID unsignedCharValue];
}

- (UInt8)algID {
    //SP 800-78-4 Table 6-2 and 6-3
    if ([self.keyType isEqual:(id)kSecAttrKeyTypeECSECPrimeRandom]) {
        switch (self.keySizeInBits) {
            case 256:
                return 0x11; //EC 256
            case 384:
                return 0x14; //EC 384
        }
    } else if ([self.keyType isEqual:(id)kSecAttrKeyTypeRSA]) {
        switch (self.keySizeInBits) {
            case 1024:
                return 0x06;    //RSA 1024
            case 2048:
                return 0x07;    //RSA 2048
        }
    }
    return 0;
}

@end

@implementation TKTokenKeychainItem(PIVDataFormat)

- (void)setName:(NSString *)name {
    if (self.label != nil) {
        self.label = [NSString stringWithFormat:@"%@ (%@)", name, self.label];
    } else {
        self.label = name;
    }
}

@end

@implementation TKSmartCard(PIVDataFormat)

- (TKTLVRecord *)sendIns:(UInt8)ins p1:(UInt8)p1 p2:(UInt8)p2 request:(TKTLVRecord *)request expectedTag:(TKTLVTag)expectedTag sw:(UInt16 *)sw error:(NSError * _Nullable __autoreleasing *)error {
    *sw = 0;
    NSData *replyData = [self sendIns:ins p1:p1 p2:p2 data:request.data le:@0 sw:sw error:error];
    if (replyData.length == 0) {
        if (error != nil && replyData != nil && (*sw == 0x9000 || *sw == 0x6a82 || *sw == 0x6a80)) {
            *error = [NSError errorWithDomain:TKErrorDomain code:TKErrorCodeObjectNotFound userInfo:nil];
        }
        return nil;
    }

    TKTLVRecord *response = [TKBERTLVRecord recordFromData:replyData];
    if (response.tag != expectedTag) {
        os_log_error(OS_LOG_DEFAULT, "expecting response with tag 0x%x, got %@", (unsigned)expectedTag, response);
        if (error != nil) {
            *error = [NSError errorWithDomain:TKErrorDomain code:TKErrorCodeCorruptedData userInfo:nil];
        }
        return nil;
    }

    return response;
}

- (nullable NSArray<TKTLVRecord *> *)recordsOfObject:(TKTokenObjectID)objectID error:(NSError **)error {
    if (![objectID isKindOfClass:NSData.class]) {
        if (error != nil) {
            *error = [NSError errorWithDomain:TKErrorDomain code:TKErrorCodeObjectNotFound userInfo:nil];
        }
        return nil;
    }

    os_log_debug(OS_LOG_DEFAULT, "reading card object %@", objectID);
    TKTLVRecord *request = [[TKBERTLVRecord alloc] initWithTag:0x5c value:(NSData *)objectID];
    UInt16 sw;
    TKTLVRecord *response = [self sendIns:0xcb p1:0x3f p2:0xff request:request expectedTag:0x53 sw:&sw error:error];
    if (response == nil) {
        return nil;
    }

    NSArray<TKTLVRecord *> *records = [TKBERTLVRecord sequenceOfRecordsFromData:response.value];
    if (records == nil) {
        os_log_error(OS_LOG_DEFAULT, "read data object has incorrect structure");
        if (error != nil) {
            *error = [NSError errorWithDomain:TKErrorDomain code:TKErrorCodeCorruptedData userInfo:nil];
        }
    }
    return records;
}

@end

@implementation PIVToken

- (nullable NSData *)dataOfCertificate:(TKTokenObjectID)certificateObjectID smartCard:(TKSmartCard *)smartCard error:(NSError * _Nullable __autoreleasing *)error {
    // Read certificate records from the card.
    NSArray<TKTLVRecord *> *certificateRecords = [smartCard recordsOfObject:certificateObjectID error:error];
    if (certificateRecords == nil) {
        return nil;
    }

    // Process certificate records, extract data and info field.
    __block NSData *certificateData;
    __block BOOL compressed = NO;
    [certificateRecords enumerateObjectsUsingBlock:^(TKTLVRecord * _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
        if (obj.tag == 0x70) {
            certificateData = obj.value;
        } else if (obj.tag == 0x71 && obj.value.length > 0) {
            UInt8 info = *(const UInt8 *)obj.value.bytes;
            if ((info & 0x01) != 0) {
                compressed = YES;
            }
        }
    }];
    if (certificateData == nil) {
        if (error != nil) {
            *error = [NSError errorWithDomain:TKErrorDomain code:TKErrorCodeObjectNotFound userInfo:nil];
        }
        return nil;
    }

    return compressed ? [certificateData inflate] : certificateData;
}

- (BOOL)populateIdentityFromSmartCard:(TKSmartCard *)smartCard into:(NSMutableArray<TKTokenKeychainItem *> *)items certificateTag:(TKTLVTag)certificateTag name:(NSString *)certificateName keyTag:(TKTLVTag)keyTag name:(NSString *)keyName sign:(BOOL)sign keyManagement:(BOOL)keyManagement alwaysAuthenticate:(BOOL)alwaysAuthenticate error:(NSError **)error {
    // Read certificate data.
    TKTokenObjectID certificateID = [TKBERTLVRecord dataForTag:certificateTag];
    NSData *certificateData = [self dataOfCertificate:certificateID smartCard:smartCard error:error];
    if (certificateData == nil) {
        // If certificate cannot be found, just silently skip the operation, otherwise report an error.
        return (error != nil && [(*error).domain isEqual:TKErrorDomain] && (*error).code == TKErrorCodeObjectNotFound);
    }

    // Create certificate item.
    id certificate = CFBridgingRelease(SecCertificateCreateWithData(kCFAllocatorDefault, (CFDataRef)certificateData));
    if (certificate == NULL) {
        if (error != nil) {
            *error = [NSError errorWithDomain:TKErrorDomain code:TKErrorCodeCorruptedData userInfo:@{NSLocalizedDescriptionKey: NSLocalizedString(@"CORRUPTED_CERT", nil)}];
        }
        return NO;
    }
    TKTokenKeychainCertificate *certificateItem = [[TKTokenKeychainCertificate alloc] initWithCertificate:(__bridge SecCertificateRef)certificate objectID:certificateID];
    if (certificateItem == nil) {
        return NO;
    }
    [certificateItem setName:certificateName];

    // Create key item.
    TKTokenKeychainKey *keyItem = [[PIVTokenKeychainKey alloc] initWithCertificate:(__bridge SecCertificateRef)certificate objectID:@(keyTag) certificateID:certificateItem.objectID alwaysAuthenticate:alwaysAuthenticate];
    if (keyItem == nil) {
        return NO;
    }
    [keyItem setName:keyName];

    NSMutableDictionary<NSNumber *, TKTokenOperationConstraint> *constraints = [NSMutableDictionary dictionary];
    keyItem.canSign = sign;
    keyItem.suitableForLogin = sign;
    TKTokenOperationConstraint constraint = alwaysAuthenticate ? PIVConstraintPINAlways : PIVConstraintPIN;
    if (sign) {
        constraints[@(TKTokenOperationSignData)] = constraint;
    }
    if ([keyItem.keyType isEqual:(id)kSecAttrKeyTypeRSA]) {
        keyItem.canDecrypt = keyManagement;
        if (keyManagement) {
            constraints[@(TKTokenOperationDecryptData)] = constraint;
        }
    } else if ([keyItem.keyType isEqual:(id)kSecAttrKeyTypeECSECPrimeRandom]) {
        keyItem.canPerformKeyExchange = keyManagement;
        if (keyManagement) {
            constraints[@(TKTokenOperationPerformKeyExchange)] = constraint;
        }
    }
    keyItem.constraints = constraints;
    [items addObject:certificateItem];
    [items addObject:keyItem];
    return YES;
}

- (nullable instancetype)initWithSmartCard:(TKSmartCard *)smartCard AID:(nullable NSData *)AID PIVDriver:(PIVTokenDriver *)tokenDriver error:(NSError **)error {
    // Read and parse Card Holder Unique Identifier.
    NSArray<TKTLVRecord *> *chuid = [smartCard recordsOfObject:[TKBERTLVRecord dataForTag:0x5fc102] error:error];
    if (chuid == nil) {
        os_log_error(OS_LOG_DEFAULT, "failed to read CHUID record (%@)", error ? *error : nil);
        return nil;
    }

    // Find Card GUID in CHUID.
    __block NSString *instanceID;
    [chuid enumerateObjectsUsingBlock:^(TKTLVRecord * _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
        if (obj.tag == 0x34) {
            instanceID = [obj.value hexString];
            *stop = YES;
        }
    }];
    if (instanceID == nil || instanceID.length == 0) {
        if (error) {
            *error = [NSError errorWithDomain:TKErrorDomain code:TKErrorCodeObjectNotFound userInfo:nil];
            os_log_error(OS_LOG_DEFAULT, "CHUID record does not contain Card GUID");
        }
        return nil;
    }

    if (self = [super initWithSmartCard:smartCard AID:AID instanceID:instanceID tokenDriver:tokenDriver]) {
        // Find out how many on-card key history objects are present, use Key History object.
        __block NSInteger onCardKeyHistoryCount = 0;
        NSArray<TKTLVRecord *> *keyHistory = [smartCard recordsOfObject:[TKBERTLVRecord dataForTag:0x5fc10c] error:error];
        if (keyHistory != nil) {
            [keyHistory enumerateObjectsUsingBlock:^(TKTLVRecord * _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
                if (obj.tag == 0xc1 && obj.value.length > 0) {
                    onCardKeyHistoryCount = *(const UInt8 *)obj.value.bytes;
                    *stop = YES;
                }
            }];
        } else if (error != nil && (*error).code != TKErrorCodeObjectNotFound) {
            return nil;
        }

        // Prepare array with keychain items representing on card objects.
        NSMutableArray<TKTokenKeychainItem *> *items = [NSMutableArray arrayWithCapacity:4 + onCardKeyHistoryCount];
        if (![self populateIdentityFromSmartCard:smartCard into:items certificateTag:0x5fc105 name:NSLocalizedString(@"PIV_AUTH_CERT", nil) keyTag:0x9a name:NSLocalizedString(@"PIV_AUTH_KEY", nil) sign:YES keyManagement:NO alwaysAuthenticate:NO error:error] ||
            ![self populateIdentityFromSmartCard:smartCard into:items certificateTag:0x5fc101 name:NSLocalizedString(@"CARD_AUTH_CERT", nil) keyTag:0x9e name:NSLocalizedString(@"CARD_AUTH_KEY", nil) sign:YES keyManagement:NO alwaysAuthenticate:NO error:error] ||
            ![self populateIdentityFromSmartCard:smartCard into:items certificateTag:0x5fc10a name:NSLocalizedString(@"DIG_SIG_CERT", nil) keyTag:0x9c name:NSLocalizedString(@"DIG_SIG_KEY", nil) sign:YES keyManagement:NO alwaysAuthenticate:YES error:error] ||
            ![self populateIdentityFromSmartCard:smartCard into:items certificateTag:0x5fc10b name:NSLocalizedString(@"KEY_MGMT_CERT", nil) keyTag:0x9d name:NSLocalizedString(@"KEY_MGMT_KEY", nil) sign:NO keyManagement:YES alwaysAuthenticate:NO error:error]) {
            return nil;
        }
        for (NSInteger i = 0; i < onCardKeyHistoryCount; i++) {
            NSString *certificateName = [NSString stringWithFormat:NSLocalizedString(@"RET_KEY_MGMT_CERT", nil), (long)i + 1];
            NSString *keyName = [NSString stringWithFormat:NSLocalizedString(@"RET_KEY_MGMT_KEY", nil), (long)i + 1];
            if (![self populateIdentityFromSmartCard:smartCard into:items certificateTag:0x5fc10d + i name:certificateName keyTag:0x82 + i name:keyName sign:NO keyManagement:YES alwaysAuthenticate:NO error:error]) {
                return nil;
            }
        }

        // Populate keychain state with keys.
        [self.keychainContents fillWithItems:items];
    }

    return self;
}

- (TKTokenSession *)token:(TKToken *)token createSessionWithError:(NSError * _Nullable __autoreleasing *)error {
    return [[PIVTokenSession alloc] initWithToken:self];
}

@end
```

[Next](PIVToken-TokenDriver.m.md)[Previous](PIVToken-NSDataZip.m.md)

