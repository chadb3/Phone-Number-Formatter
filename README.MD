# Correct Phone Number
 This is to correct phone numbers. Some software won't accept phone numbers variants like: (555) 234-5678 or 555-234-5678

 This will correct it down to 5552345678

 Using this will reduce errors that could be introduced by manually typing the numbers.

 Now prints a "Human Readable: 555-234-5678" if the input number was like "5552345678". (Also works with phonewords)

 Most Functionality is now integrated into my call logger python program.

 Now translates phonewords by default!

## How To Use:
 
After you enter the "phone number" hit enter
```

Enter Phone Number: (555) 234-5678
Before: (555) 234-5678

After: 5552345678

Outgoing Format: 15552345678

```
Basic Example 2:
```

Enter Phone Number: 5552345678
Human Readable: 555-234-5678

Human Readable: 555-234-5678


After: 5552345678

Outgoing Format: 15552345678

```

Phoneword Example:
```

Enter Phone Number: (555) ADG-JMPT
Required Translation: True
Before: (555) 234-5678

After: 5552345678

Outgoing Format: 15552345678

```

Phoneword Example 2:
```

Enter Phone Number: 555ADGJMPT
Human Readable: 555-ADG-JMPT

Required Translation: True
Human Readable: 555-234-5678


After: 5552345678

Outgoing Format: 15552345678

```