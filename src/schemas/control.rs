use serde::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct VelocityCommand {
    pub linear: f32,
    pub angular: f32,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct CommandMeta {
    pub source: String,
    pub timestamp: u64,
    pub command_id: String,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct ControlMessage {
    pub velocity: VelocityCommand,
    pub meta: CommandMeta,
}
