Captcha relies on hard AI problems. This means problens which our human brian can solve easily due to pattern recognition, but an AI would struggle immensely to solve. 

--> Key Components
    Challenge Generator: This creates a tough problem. It could be divided image recognition, distorted text analysis etc.
    Validation Engine: Compares the output of the user to a set truth, typically provides a score
    Telemetry tracker: An additional layer of security wherein the Captcha monitors the physicl mouse movements, etc. to gauge if a human is answering.

--> An effective CAPTCHA uses a Challenge-Response / Verification architecture
    Request Trigger: A user attempts an action like signing up. The web server requests a token from the captcha service.
    Challenge Delivery: The service sends a unique, encrypted payload to the user’s browser.
    Client Execution: The user solves the puzzle. Simultaneously, a program records telemetry for analysis.
    Verification: The solution and telemetry are sent to the Validation Server. This typically returns a probability score.
    Access Grant: If score > 0.8, the transaction proceeds. else, it triggers a harder challenge or a block.
    
--> The combination of the actual puzzle and the telemetry analysis makes sure that passing the captcha is monumentally difficult for an AI system. It targets what AI specifically struggles to do.
    
    
    
