# Username Generator

A feature that generates a unique bootcamp username based on a format and personal information.

## Program Structure

1. The program should prompt a user to input their:
   - First Name
   - Last Name
   - Campus
   - Cohort Year
   
   *It is your choice whether to collect this input one by one or in a single string.*

2. The program should validate user input in the following ways:
   - First name and last name should not contain digits.
   - Campus should be a valid campus.
   - Cohort year should be a valid cohort year (a candidate cannot join a cohort in the past).

3. A function will generate the username based on the provided input.

4. The user will then be asked if the final username is correct. They should be informed of the username format before confirming correctness.

## Example

**Input:**
- First Name: Lungelo
- Last Name: Mkhize
- Cohort Year: 2025
- Final Campus: Durban

**Generated Username:**
`elomkhDBN2025`

### Username Format:
- **ELO** - Last 3 letters of the first name (if the name is shorter than 3 letters, append 'O' at the end).
- **MKH** - First 3 letters of the last name.
- **DBN** - Abbreviation of the selected campus.
- **2025** - Cohort year.

This ensures each username follows a standardized and unique format for bootcamp participants.

