const express = require("express");
const cors = require("cors");
const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, ScanCommand } = require("@aws-sdk/lib-dynamodb");
const app = express();
app.use(cors());
const client = new DynamoDBClient({
region: "ap-south-1"
});
const docClient = DynamoDBDocumentClient.from(client);
app.get("/api/files", async (req, res) => {
try {
const result = await docClient.send(
new ScanCommand({
TableName: "CloudAssignmentTable"
})
);
res.json(result.Items || []);
} catch (err) {
res.status(500).json({ error: err.message });
}
});
app.listen(3000, () => {
console.log("Server started on port 3000");
});
