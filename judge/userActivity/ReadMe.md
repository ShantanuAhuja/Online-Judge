# 🧾 User Submissions & Leaderboard (Summary)

## 📤 User Submissions (`/submissions`)
- **Purpose**: Shows the latest 10 submissions by the logged-in user.
- **Template**: `userSubmissions.html`
- **Authentication**: Required
- **Key Info**: Displays verdicts, language, and timestamps.

## 📄 Particular Submission (`/submission/<id>`)
- **Purpose**: Displays code content and metadata for a specific submission.
- **Template**: `particularCodeSubmission.html`
- **Authentication**: Required
- **Key Info**: Reads and displays code file; handles missing files.

## 🏆 Leaderboard (`/leaderboard`)
- **Purpose**: Ranks users based on unique accepted problems.
- **Template**: `leaderboard.html`
- **Scoring**: `score = 100 * (unique accepted problems)`
- **Key Info**: Users sorted by score in descending order.

