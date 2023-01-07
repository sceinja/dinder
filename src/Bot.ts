import { Client } from "discord.js";
import ready from "./listeners/ready";

const token = '';

console.log("Dinder is starting . . .");

const client = new Client({
    intents: []
});

ready(client)

client.login(token);

console.log(client);
