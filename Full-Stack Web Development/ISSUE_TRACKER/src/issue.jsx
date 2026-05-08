import React from 'react';

const issues = [
  { id: 1, title: 'Bug in Login', description: 'Error 404 on login', status: 'Open' },
  { id: 2, title: 'UI Issue on Dashboard', description: 'Misaligned elements', status: 'Closed' },
  { id: 3, title: 'API Timeout', description: 'Delayed response from server', status: 'Open' },
];

function IssueList() {
  return (
    <div>
      <h1>Issue Tracker</h1>
      <ul> {/* Wrap list items inside an unordered list */}
        {issues.map(issue => (
          <li key={issue.id}> {/* Correctly assign 'key' inside <li> */}
            <h2>{issue.title}</h2> {/* Use curly braces to display the title */}
            <p>{issue.description}</p> {/* Use curly braces to display the description */}
            <p>Status: {issue.status}</p> {/* Use curly braces to display the status */}
          </li>
        ))}
      </ul>
    </div>
  );
}
export default IssueList;
