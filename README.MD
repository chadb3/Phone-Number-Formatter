# Correct Phone Number
 This is to correct phone numbers. Some software won't accept phone numbers variants like: (202) 555-0100 or 202-555-0100

 This will correct it down to 2025550100

 Using this will reduce errors that could be introduced by manually typing the numbers.

 Now prints a "Human Readable: 555-555-0199" if the input number was like "5555550199". (Also works with phonewords)

 Most Functionality is now integrated into my call logger python program.

 Now translates phonewords by default!

## How To Use:
 
After you enter the "phone number" hit enter
```

Enter Phone Number: 202-555-0199
Before: 202-555-0199

After: 2025550199

Outgoing Format: 12025550199

```
Basic Example 2:
```

Enter Phone Number: 5555550199
Human Readable: 555-555-0199

Human Readable: 555-555-0199


After: 5555550199

Outgoing Format: 15555550199

```

Phoneword Example:
```

Enter Phone Number: 555-JJK-01GO
Required Translation: True
Before: 555-555-0146

After: 5555550146

Outgoing Format: 15555550146

```

Phoneword Example 2:
```

Enter Phone Number: 555JJK01GO
Human Readable: 555-JJK-01GO

Required Translation: True
Human Readable: 555-555-0146


After: 5555550146

Outgoing Format: 15555550146

```
