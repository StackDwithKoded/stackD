// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.28;

contract Starter{

    address public owner;
    string private secretMessage;

    event MessageUpdated(string newMessage);

    constructor(string memory _initialMessage) {
        owner = msg.sender;
        secretMessage = _initialMessage;
    }

    // 5. Function Modifier (A reusable piece of logic to restrict access)
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner!");
        _; // This underscore tells Solidity to execute the rest of the function
    }

    // 6. Public Function (Anyone can call this to read the message)
    function getMessage() public view returns (string memory) {
        return secretMessage;
    }

    // 7. Restricted Function (Only the owner can call this)
    function updateMessage(string memory _newMessage) public onlyOwner {
        secretMessage = _newMessage;
        emit MessageUpdated(_newMessage);
    }

}



// INSTANCE / USAGE

// Calling the function withdraw
// withdraw(40TETH)