Feature: Testing the pricing function for text to be translated

  Scenario: Valuation of the translation service
      Given Start browser
      When The user clicks button
      And  The user enters the text and selects the target language
      And  The user selects additional options
      Then The application will respond with the time and cost of the service