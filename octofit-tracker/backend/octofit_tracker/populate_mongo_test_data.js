db = db.getSiblingDB('octofit_db');

db.users.deleteMany({});
db.teams.deleteMany({});
db.activity.deleteMany({});
db.leaderboard.deleteMany({});
db.workouts.deleteMany({});

db.users.insertMany([
  { email: 'alice@example.com', name: 'Alice', password: 'alicepass' },
  { email: 'bob@example.com', name: 'Bob', password: 'bobpass' },
  { email: 'carol@example.com', name: 'Carol', password: 'carolpass' }
]);

db.teams.insertMany([
  { name: 'Team Alpha', members: [
    { email: 'alice@example.com', name: 'Alice' },
    { email: 'bob@example.com', name: 'Bob' }
  ]},
  { name: 'Team Beta', members: [
    { email: 'carol@example.com', name: 'Carol' }
  ]}
]);

db.activity.insertMany([
  { user_email: 'alice@example.com', activity_type: 'run', duration: 30, date: new Date() },
  { user_email: 'bob@example.com', activity_type: 'walk', duration: 45, date: new Date() },
  { user_email: 'carol@example.com', activity_type: 'strength', duration: 20, date: new Date() }
]);

db.workouts.insertMany([
  { name: 'Pushups', description: 'Do 20 pushups' },
  { name: 'Situps', description: 'Do 30 situps' }
]);

db.leaderboard.insertMany([
  { team_name: 'Team Alpha', points: 100 },
  { team_name: 'Team Beta', points: 80 }
]);
