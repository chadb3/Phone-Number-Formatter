# phoneNumber README

This is used to store the parts of the Phone_Number object.

## parts of Phone_Number

### public variables

- phone_number_as_entered
- paste_friendly
- country_code
- area_code
- central_office_code
- line_number
- human_readable
- outgoingFormat


### public functions


- printPhoneNumber()
- getPhoneNumber()

## About Variables 

- phone_numbered_as_entered
```
The exact string as entered.
```

- paste_friendly
```
holds phone number without any formatting 
```

- country_code
- area_code
- central_office_code
- line_number
```
each one holds part of the phone number
```

- human_readable
```
holds "human readable" format (with dashes)
```

- outgoingFormat
```
paste_friendly but with a one appended to the front
```

## About Functions

- printPhoneNumber()
```
prints 
phone_number_as_entered
paste_friendly
human_readable
outgoingFormat
```

- getPhoneNumber()
```
 returns [country_code,area_code,central_office_code,line_number]
```
note: returns as a array