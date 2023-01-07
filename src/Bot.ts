import { Client } from "discord.js";
import ready from "./listeners/ready";

const token = 'MTA1NjQxMjk5OTkzMTM5NjIwNw.Gp5h9r.KhrfCWqrVLR4YLdxBVF5hz_q49ERHmceywJY3w';

console.log("Dinder is starting . . .");

const client = new Client({
    intents: []
});

ready(client)

client.login(token);

console.log(client);