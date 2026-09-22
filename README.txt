# Applied Agentic AI — Experiments 3, 5 & 8

---

# Experiment 3: Prompt Chaining for Summarization

## Aim

To implement a multi-step prompt chaining workflow for generating accurate and structured summaries.

## Objective

* Divide a complex summarization task into multiple steps.
* Process information sequentially.
* Maintain information between stages.
* Generate a concise final summary.

## Technologies Used

* Python
* Large Language Model (LLM)
* Prompt Engineering
* Prompt Chaining

## Workflow

The system uses a **6-stage sequential pipeline**:

1. **Input Collection** — Receive the original text.
2. **Text Analysis** — Identify important information.
3. **Key Point Extraction** — Extract the main ideas.
4. **Intermediate Summary** — Create an initial summary.
5. **Refinement** — Improve clarity and remove unnecessary information.
6. **Final Summary** — Generate the final structured summary.

## Example

**Input:**

```text
Artificial Intelligence is transforming many industries.
It is used in healthcare, banking, education, cybersecurity,
and transportation to automate tasks and support decision-making.
```

**Final Summary:**

```text
Artificial Intelligence is widely used across industries
to automate tasks and improve decision-making.
```

## Result

The prompt chaining workflow successfully generates a concise and structured summary.

## Conclusion

This experiment demonstrates how a complex task can be divided into smaller sequential prompts to improve the quality and organization of the final output.

---

# Experiment 5: Multi-Agent SDR System

## Aim

To develop a multi-agent system that automates sales development activities such as lead generation, lead qualification, and email drafting.

## Objective

* Generate potential leads.
* Analyze and qualify leads.
* Assign specialized tasks to different agents.
* Create personalized email drafts.
* Demonstrate collaboration between multiple AI agents.

## Technologies Used

* Python
* AI Agents
* Multi-Agent Systems
* Natural Language Processing
* Prompt Engineering

## Agents Used

### 1. Lead Generation Agent

Identifies potential customers or leads based on given requirements.

### 2. Lead Qualification Agent

Analyzes leads and determines whether they match the required criteria.

### 3. Email Drafting Agent

Creates personalized email drafts for qualified leads.

## Workflow

```text
User Requirements
       ↓
Lead Generation Agent
       ↓
Lead Qualification Agent
       ↓
Email Drafting Agent
       ↓
Final Email Draft
```

## Example

**Input:**

```text
Find potential customers interested in AI cybersecurity solutions.
```

**Lead Generation:**

```text
Lead: ABC Technologies
Interest: AI and Cybersecurity
```

**Lead Qualification:**
``
