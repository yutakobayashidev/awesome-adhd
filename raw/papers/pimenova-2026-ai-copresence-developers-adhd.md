---
source_url: https://arxiv.org/abs/2609.21254v1
ingested: 2026-09-21
sha256: 6a2a31cfcb2d93f1886d3b00c0c97e5a2896d0fa36ebf14f058125d8e2977f9e
arxiv_id: 2609.21254v1
doi: null
---

# Two's a Crowd: Human and AI-Based Copresence for Developers with ADHD

Source: https://arxiv.org/abs/2609.21254v1  
PDF: https://arxiv.org/pdf/2609.21254v1  
arXiv ID: 2609.21254v1  
Published: 2026-09-18  
Authors: Veronica Pimenova, Seth Bernstein, Shalini Madan, Dhruv Jain, Venkatesh Potluri  
Categories: cs.HC, cs.SE

## Automation curation note

Selected by the research-watch curation job because it directly covers adult ADHD, software work, body doubling/copresence, AI coding assistants, task initiation, flow, privacy, and inclusive developer productivity. Score: 3 (raw + existing page updates). This is a qualitative interview/preprint source, not clinical treatment evidence.

## Extracted paper text

```text
arXiv:2609.21254v1 [cs.HC] 18 Sep 2026

Two’s a Crowd: Human and AI-Based Copresence for Developers
with ADHD
VERONICA PIMENOVA, University of Michigan, USA
SETH BERNSTEIN, University of Michigan, USA
SHALINI MADAN, University of Michigan, USA
DHRUV JAIN, University of Michigan, USA
VENKATESH POTLURI, University of Michigan, USA
Effective collaboration and communication are vital to developer productivity and well-being, yet remain constrained
by human factors such as attention, intrinsic motivation, and interpersonal accountability. These constraints are
particularly vital for developers identifying with Attention Deficit Hyperactivity Disorder (ADHD), who navigate
persistent environmental barriers in modern hybrid workplace settings. While developers with ADHD frequently rely
on collaborative copresence practices (such as body doubling or pair programming) to support executive function, the
recent emergence of agentic AI coding assistants has begun reshaping these collaborative dynamics. To investigate
how developers with ADHD engage in human and AI-based copresence practices, we conducted semi-structured
interviews with 14 software engineers with ADHD. Our findings reveal that while traditional human-human copresence
provides critical social support and onboarding structure, it forces developers to constantly manage professional
reputation and sacrifice personal privacy. Conversely, developers leverage emerging human-AI copresence to maintain
accountability and cognitive flow without the social anxiety, performance judgment, or surveillance associated with
human observation. Based on these empirical insights, we map developer copresence practices onto core dimensions of
Goffman’s copresence theory and Forsgren et al.’s SPACE framework of developer productivity, and provide design
recommendations for AI-based tools that promote inclusive collaboration for developers with ADHD.
CCS Concepts: • Human-centered computing → Accessibility; • Software and its engineering → Collaboration in
software development.
Additional Key Words and Phrases: ADHD, Teamwork, Software engineering, Productivity, Well-being

1

Introduction

Effective collaboration and communication among developers are vital to the productivity and success
of software development teams [25, 30, 59]. Traditional collaboration and communication patterns have
changed rapidly with the rise of hybrid workplace practices and the widespread adoption of agentic, artificial
intelligence (AI) software development tools [29, 51]. In this evolving workplace, human factors such as
sustained attention, intrinsic motivation, and interpersonal accountability have become critical determinants
Authors’ Contact Information: Veronica Pimenova, University of Michigan, Ann Arbor, Michigan, USA, pimenova@umich.edu; Seth
Bernstein, University of Michigan, Ann Arbor, Michigan, USA, sethbern@umich.edu; Shalini Madan, University of Michigan, Ann
Arbor, Michigan, USA, shalinii@umich.edu; Dhruv Jain, University of Michigan, Ann Arbor, Michigan, USA, profdj@umich.edu;
Venkatesh Potluri, University of Michigan, Ann Arbor, Michigan, USA, potluriv@umich.edu.

1

2

Pimenova et al.

Fig. 1. Modalities of copresence practices for developers with ADHD: (A) human-AI copresence; (B) human-human
copresence; (C) human-AI-human copresence.

of overall developer productivity and well-being [82, 87], as measured by Forsgren et al.’s SPACE framework
for developer productivity (a widely-used metric in software engineering communities) [30].
Human factors are especially prevalent for the approximately 10.57% of developers globally identifying
with Attention Deficit Hyperactivity Disorder (ADHD) [80]. While professionals with ADHD possess
distinct cognitive strengths, including high levels of creativity and the ability to hyperfocus when working
independently [10, 81, 92], these traits are frequently disrupted by workplace-induced environmental
barriers. Unstructured workplace cues and fragmented, asynchronous communication forces developers
with ADHD into continuous, exhausting self-regulation [18, 63]. This ongoing environmental mismatch
between cognitive needs and workplace demands contributes to lower job satisfaction, higher burnout, and
increased rates of involuntary job termination [44, 58]
To navigate these environmental barriers, professionals with ADHD frequently turn to copresence-based
collaborative strategies such as body doubling in general daily contexts and pair programming within code
development contexts [4, 93]. Copresence involves leveraging the physical or virtual presence of another
individual to enhance task initiation, self-regulation, and accountability during focus periods [14, 34]. In
software engineering, pair programming similarly bridges executive function gaps by providing real-time
cognitive support during complex tasks such as debugging or architecture planning [3, 63]. As developers
increasingly adopt agentic coding assistants as synthetic partners in AI-based co-creation [66, 70], copresence
is expanding beyond human-human dynamics to include human-AI collaboration. However, while traditional
human-human copresence provides critical social-emotional and accountability support, it remains unclear
how these dynamics translate when the copresence partner is an AI agent or how AI tools enhance
human-human collaboration.
To address this gap, our study investigates the following research questions:
• RQ1: How do software engineers with ADHD currently engage in copresence practices across
human-human and human-AI collaboration settings?
• RQ2: What challenges do developers with ADHD experience during copresence practices, and
what strategies do they employ to maintain focus and flow across human-human and human-AI
copresence practices?

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

3

• RQ3: How can AI-based tools be designed to enhance copresence practices–both as partners in
human-AI collaboration and as facilitators of human-human collaboration?
Through semi-structured interviews with 14 software engineers with ADHD, we uncover how developers
navigate mutual copresence practices across physical, remote, and AI-mediated settings. We reveal that while
in-person copresence practices such as body doubling provide social accountability and task initiation, they
often introduce anxiety related to job performance. Conversely, while agentic AI tools offer judgment-free
technical pairing and real-time feedback, uncoordinated AI usage increases cognitive load and disrupts
shared mental models. Finally, we highlight how developers establish boundaries where AI agents succeed
as ambient focus tools and where human expertise remains.
In summary, we contribute:
• Empirical findings from semi-structured interviews with 14 developers with ADHD detailing
how developers navigate executive dysfunction, task initiation barriers, and social anxiety during
human-human and human-AI copresence sessions.
• Theoretical mapping of collaborative copresence practices, challenges and AI workflows onto
copresence theory, structured around dimensions of Forsgren et al.’s SPACE framework.
• Design implications for AI-based copresence tools that balance productivity with emotional and
cognitive well-being for developers with ADHD.
2

Background & Related Work

We contextualize our work within four areas of prior literature: (1) ADHD in workplace settings, (2) the
theoretical foundations of copresence and body doubling, (3) collaborative practices in software engineering,
and (4) prior work on developers with ADHD.
2.1

ADHD in Workplace Settings

ADHD is a cognitive, neurodevelopmental condition in which individuals experience high levels of creativity,
divergent thinking, and hyperfocus (a state of deep, immersive engagement with complex tasks) [10, 41,
64, 74]. Beyond individual cognition, the differences between individuals with ADHD and neuro-typical
individuals influence how professionals with ADHD navigate social and collaborative workplace settings [7].
Workplace functioning for adults with ADHD is often shaped less by ability alone and more by organizational
structure, where organizational demands such as strict deadlines, multitasking, and low external scaffolding
can exacerbate executive function challenges, leading to disproportionate negative effects [61].
Adults with ADHD experience higher rates of unemployment and significant barriers in occupational
functioning in traditional workplace settings, including increased job burnout characterized by higher emotional, cognitive, and physical exhaustion [45, 88]. These environmental constraints prevent professionals
with ADHD from leveraging their strengths (such as creativity or hyperfocus [10, 41, 74]) in workplace

4

Pimenova et al.

settings. Following the Social Model of Disability [36, 76], we frame these barriers not as individual deficits,
but as the result of social and physical barriers created within traditional workplace environments [6, 8].
A lack of structured workplace cues often forces professionals with ADHD to perform invisible access
labor: the additional, unacknowledged mental effort required to adapt neurotypical workplace systems
to meet their own cognitive needs [12, 18, 91]. Das et al. explored how in remote work environments,
the "invisible" nature of ADHD can lead to a lack of structured workplace support, forcing professionals
to perform invisible access labor to maintain a balance between meeting performance expectations and
managing their own mental energy [18]. Ezeamii et al. similarly find that PhD students with ADHD engage
in invisible labor to navigate rigid academic structures by developing personalized workflows, relying on
informal support networks, and avoiding stigmatized formal accommodations [26]. The invisible labor
required by ADHD professionals in workplace settings creates significant friction in balancing productivity
and well-being, where Pimenova et al. explored how professionals with ADHD experience strenuous
invisible access labor and create their own "hacks" to assistive technology just to access everyday workplace
communication systems [67]. Marathe and Piper expand the concept of invisible access labor into the
accessibility paradox: while companies actively seek to hire and retain disabled workers, reliance on productdriven goals and normative productivity metrics leads to the de-prioritization of internal tool accessibility,
forcing disabled employees to perform invisible labor [55].
Furthermore, the lack of physical copresence in digital spaces such as Zoom can increase invisible
access labor, leading to isolation or workplace friction [51, 94]. Duckert and Bjørn show that the spatial
instability inherent in hybrid work introduces "location multiplicity"—an unpredictability in physical office
attendance that causes workers to default to digital tools, turning physical office spaces into a lost space
and compounding the difficulty of maintaining shared awareness [22]. Conversely, Meyer and Fritz show
that cultivating shared schedule awareness and unified presence displays in hybrid teams can mediate
intrusive interruptions, allowing knowledge workers to better protect deep focus time while maintaining
effective teamwork [56]. These mismatches are especially prevalent in software engineering settings, where
approximately 10.57% of software engineers identify as having ADHD [80, 89]. Many developers with
ADHD find that a lack of structured, physical workplace cues creates a reliance on internal self-regulation
that is difficult to sustain [31, 62, 63]. This highlights a critical gap in the exploration of how collaborative
practices in workplace settings can be changed to reduce invisible access labor and promote well-being for
developers with ADHD.
2.2

Copresence and body doubling

Previous literature in the field of social and behavioral psychology has defined the action of an individual "being together" with another individual as the term copresence [34, 97], which creates a sense of a
shared environment for two individuals. Campos-Castillo and Hitlin breaks copresence into three primary
components: mutual attention, mutual emotion, and mutual behavior [14]. Mutual attention refers to two
individuals who are "reciprocally focused on one another", mutual emotion refers to the sharing of the

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

5

other person’s emotion through conscious awareness, and mutual behavior refers to a combined behavior
pattern in which one person mimics another’s motor activity [14]. This sense of "mutual togetherness"
can be extended beyond physical presence to virtual environments [5, 73, 77, 83, 84]. This can happen in
digital environments through virtual avatars, online Zoom calls, or asynchronous settings such as chat
rooms [37, 43, 49, 72, 85].
A specific manifestation of copresence which has gained significant traction within the ADHD community
is body doubling, where an individual performs a task in the presence of another person (the “body doubling
partner”) [1, 11]. This practice increases motivation for task completion through a shared sense of "working
alongside" another [1, 23]. Eagle et al. explored how body doubling practices provide a non-judgmental
accountability structure for individuals with broader neurodivergence, including ADHD [23, 24]. Arnold
et al. demonstrated the effectiveness of body doubling for students in post-secondary education as a tool
to manage academic load [4]. In software engineering contexts, where tasks such as debugging involve
extended periods of cognitive demand, these mechanisms may be particularly valuable [30]. However, while
high-intensity collaborative practices such as pair programming are well-documented [9], less is known
about how "low-intensity" forms of copresence, such as body doubling or virtual coworking, are leveraged
by professional developers with ADHD to navigate their daily tasks and workflow. We contribute empirical
insights into how developers with ADHD leverage low-intensity copresence modalities (body doubling and
pair programming) to manage executive function demands and support daily workflows.
2.3

Collaboration in software engineering settings

Human factors of software engineering (e.g. communication, social well-being) have increasingly become
more recognized as vital to developer productivity over technical factors (such as code output or technical performance) alone [30]. We follow Forsgren et al.’s SPACE framework of developer productivity,
which includes Satisfaction and well-being, Performance, Activity, Communication and collaboration, and
Efficiency and flow [30]. The SPACE framework is a multidimensional model for measuring developer
productivity across five key dimensions, synthesizing previous literature across fields, including areas
of human-computer interaction, software engineering, and organizational psychology [30]. Central to
this framework is the concept of "flow", a state of uninterrupted, deep focus that is essential for complex
programming tasks [30].
Further, individual developer productivity and well-being is embedded within team-level collaboration
and the social environment in which code is produced [25, 42]. Devathasan et al. describe that while
diversity in software engineering teams enhances creativity and performance, teams must first have the
ability to overcome hardship and empathy [21]. Evtikhiev et al. further emphasize that software development
collaboration is often shaped by breakdowns in communication, coordination, and knowledge sharing that
can accumulate over time and negatively impact team effectiveness [25]. Further, Miller et al. found that
remote work disrupted communication ease and reduced opportunities for informal social interaction [57].

6

Pimenova et al.
One of the most established collaborative practices in software engineering is pair programming, where

two developers work synchronously on a single task [3, 9, 93]. Begel et al. described that benefits of
pair programming include fewer bugs, higher code understanding, and higher code quality [9]. Recently
collaboration in software engineering has begun to expand beyond human partners to include AI-based
tools that directly participate in the coding process, with platforms like GitHub Copilot or ChatGPT reaching
over 15 million developers and 700 million weekly active users respectively [19]. With this recent increased
usage of AI in programming and software engineering contexts (e.g. "vibe coding") [66, 70], there is an
opportunity for developer support by pair programming with AI. Unlike human partners, AI agents scale
effortlessly, are always available, and provide a non-judgmental environment for experimentation. This
absence of social pressure is further reflected in how human-AI interaction dynamics evolve over time,
where Lazebnik et al. found that social politeness norms erode significantly faster in human-AI interactions
compared to human-human collaboration [48]. This human-AI interaction creates a new paradigm of
“AI-pair programming” where the AI can provide a form of digital copresence [53, 54, 78, 98].
Recent CSCW and HCI literature highlights how human-AI co-creation shifts collaboration patterns,
where managing agency and control mechanisms is becoming a more important measure for how effectively
users co-create alongside AI systems [40, 96]. Effective human-AI collaboration relies heavily on delegation
behavior, where Spitzer et al. demonstrated that providing clear contextual information about both human
and AI capabilities significantly improves team performance and optimizes task delegation [79]. While prior
work has extensively studied the technical accuracy of AI-generated code, there is a gap in understanding
the social and psychological impact of AI as a copresence partner, especially for those who find the social
demands of human-to-human pair programming overwhelming (such as developers with ADHD).
2.4

Prior work on developers with ADHD

Recent empirical research has begun to explore the experiences of software engineers with ADHD. Newman
et al. explored disclosure in workplace settings through a social media analysis and a large-scale survey of
software engineers with ADHD and neurodivergence more broadly, discovering both positive (workplace and
social support) and negative (workplace stigma, discrimination, extra labor) outcomes from disclosure [62].
Newman et al. also conducted a further social media analysis and survey specific to professional programmers
with ADHD and found that body doubling was used to aid time management, consistent performance, and
task initiation and completion specifically [63].
Liebel et al. interviewed software engineers with ADHD and found challenges with task deadlines,
organization and planning, and over-promising [50]. This affected developers physical and mental health,
as well as task completion and workplace productivity [50]. Strengths of developers with ADHD included
puzzle solving, creativity and divergent thinking, and the ability to "think ahead", which increased workplace
reward and task focus [50]. Gama et al. also explored neurodivergent software engineers more broadly,
interviewing four developers with ADHD on the emotional and social factors of being neurodivergent and
resulting workplace adaptations and accommodations [32].

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

7

Despite the increasing body of work identifying challenges and strengths of software engineers with
ADHD, research into collaborative interventions specifically tailored for developers with ADHD remains
limited. While Newman et al. [63] suggests that copresence practices, such as body doubling or pair
programming, could theoretically scaffold the cognitive needs of this population, there is a lack of empirical
data on how these practices are utilized in modern AI-based real-world software engineering settings. While
we understand that human factors are vital to productivity [30], we do not yet know how developers with
ADHD experience "low-intensity" copresence or how they might leverage AI agents to fulfill the role of
a body doubling partner. Our study addresses this gap by exploring the intersection of varying ADHD
cognitive styles, copresence theory, and modern AI-mediated workflows to promote software engineering
workplace environments that are inclusive and enable productivity while ensuring developer wellbeing.
3

Study Procedure

We describe our study procedure including participant recruitment, interview procedure, participant
demographics, and data analysis.
3.1

Participant recruitment

To gain deeper insights into the experiences of developers with ADHD related to copresence practices, we
conducted 14 semi-structured interviews. To be eligible for our study, participants had to be professional
software developers working in industry, have experience working on a team in an industry setting, selfidentify with or be formally diagnosed with ADHD, and located in the United States. Participants were
recruited through a variety of social media posts on platforms such as LinkedIn and X (Twitter). Participants
completed a pre-interview recruitment survey, where they described their programming experience and
current role. Additionally, participants were required to indicate that they either have a formal ADHD
diagnosis or self-identify with ADHD and score 14 or higher on the World Health Organization Adult
ADHD Self-Report Scale (ASRS) for DSM-5 [11]. We administered this scale as a screening instrument
because fewer than 20% of adults with ADHD are accurately diagnosed and treated [69], due to the barriers
to diagnosis in adult populations [75]. The scale is able to screen participants, allowing us to provide a
consistent inclusion criterion for participants without a formal diagnosis and correctly identifies 91.4% of
adults with ADHD and 96% without [45].
Our final sample included individuals with 1 – 25 years of industry experience in software development
with in-person, hybrid, and remote workplace modalities, and with 11 participants identifying as male
and 3 participants identifying as female (see Table 1 for the full participant demographic). Interviewees
were compensated with a $50 USD gift card and data collection was concluded when our sample provided
sufficient depth and diversity of perspectives to comprehensively address our research questions.

8
3.2

Pimenova et al.
Procedure

We conducted a semi-structured interview in three parts, structured around our guiding research questions.
Part one asked questions about how developers currently engage in copresence practices, specifically
focusing on body doubling and pair programming. In part two, participants shared insights into their
experiences with these practices, including the specific benefits and challenges they encounter in industry
workflows. Part three elicited responses about how an AI tool could act as a copresence partner or assist
in the facilitation of copresence sessions.1 We performed three pilot interviews to finalize our interview
protocol script. Interviews were conducted via Zoom, lasted approximately 60 minutes, and were audio-video
recorded using Zoom’s recording software. Following each session, the lead researcher created reflective
memos, and the transcripts generated by Zoom’s automatic captioning service were manually reviewed
and corrected by the researcher.
Table 1. Participant demographic data of software engineers with ADHD (𝑁 = 14)

3.3

ID

Years in Industry

Workplace Modality

Gender

Age

ADHD Diagnosis

ASRS Score

P1
P2
P3
P4
P5
P6
P7
P8
P9
P10
P11
P12
P13
P14

1 year
5 years
2 years
2 years
2 years
3 years
1 year
6 years
2 years
2 years
4 years
25 years
1 year
7 years

Hybrid
Remote
Remote
Hybrid
In-person
Hybrid
Hybrid
Hybrid
Remote
In-person
Remote
Remote
Hybrid
Hybrid

Male
Male
Male
Male
Male
Female
Male
Male
Male
Male
Male
Male
Female
Female

24
27
22
23
28
24
23
27
27
21
24
51
22
31

Self-Diagnosis
Self-Diagnosis
Formal Diagnosis
Self-Diagnosis
Formal Diagnosis
Formal Diagnosis
Self-Diagnosis
Formal Diagnosis
Formal Diagnosis
Self-Diagnosis
Self-Diagnosis
Formal Diagnosis
Formal Diagnosis
Formal Diagnosis

15
19
18
16
15
18
23
15
17
15
16
17
19
17

Data Analysis

To analyze our qualitative data, we followed Deterding and Waters’ flexible approach to thematic analysis [20], which provides an iterative, top-down approach for semi-structured interview data. This is similar
to the qualitative analysis process in related software engineering work [62, 63], where this process balances
pre-existing research goals with inductive coding and allowed us to begin with broad, conceptual indexing
mapped directly to our research questions (e.g., barriers to current copresence practices, aspects that could be
improved with AI), while remaining open to nuances within developer workflows. Our analysis progressed
1We have attempted to make the study fully replicable. A replication package containing all necessary materials, including interview

protocol and final, full codebook are available in supplementary materials of this submission. We will publicly share these files in a
Zenodo link upon acceptance.

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

9

through three stages: (1) Open coding: The 14 anonymized interview transcripts were randomly divided
among three members of the research team (the primary author and two collaborators) after the first author
created a set of initial codes based on existing research questions. Team members independently reviewed
their assigned transcripts during an initial open-coding phase to create original, descriptive codes capturing
participant behaviors and responses; (2) Visual mapping and sub-coding: To synthesize these initial codes,
the team engaged in continuous analytic memoing and met twice over a four-week period to collaboratively
group codes. We used Miro display boards to visually organize the boundaries of our sub-codes (as illustrated
in Figure 3); (3) Final code refinement: The axial coding phase allowed us to condense our original codes
into 23 distinct codes, organized into three key themes with 7–8 sub-codes per theme, ensuring sufficient
empirical detail to capture nuances of participant workflows. Following Padiyath and Nelson-Fromm [65],
we did not calculate Inter-Rater Reliability (IRR), as IRR does not align with the reflexive, interpretivist
approach to thematic analysis used, which prioritizes organic, collaborative depth over enforced consensus.
4

Findings

Fig. 2. Map of individual ADHD-related self regulatory strategies supported by collaborative practices

4.1

Modality of current copresence practices

We describe the modality of current copresence practices employed by developers with ADHD through
distinct structural modalities (§4.1.1), motivating factors contributing to developer participation in such
practices (§4.1.2), and the interpersonal partner dynamics that influence collaboration (§4.1.3).
4.1.1 Distinct structural modalities. Copresence practices are widely used in ADHD communities to support
task initiation and completion [4, 23, 24], and our participants (as developers with ADHD)2 frequently relied
2 From this point onward, when referring to "developers" or "software engineers" we refer explicitly to developers or software engineers
with ADHD. When referring to developers or software engineers without ADHD, we explicitly use the word "neurotypical".

10

Pimenova et al.

on copresence to provide the structural support that individual planning tools (e.g. Google Calendar, Notion,
personal messaging reminders) lacked.
However, participants described company-imposed environmental barriers such as unpredictable task
volumes, unclear expectations, and requirements of continuous availability frequently disrupted personal
planning and heightened performance anxiety. For example, P1 described feeling bound to their machine
due to the immediate, unannounced assignment of tasks, creating an environment of constant pressure
without adequate support systems for task initiation. Similarly, P12 highlighted the psychological weight of
on-call obligations, explaining that continuous alert notifications often trigger avoidance behaviors such as
snoozing notifications to manage the compounding stress of perpetual availability. P14 noted that corporate
complexity further complicates personal estimation of task completion time, forcing them to manually pad
schedules by several days to account for unexpected enterprise-based hurdles:
"Planning is a process where I often undershoot things. I’ve gotten better at calculating times,
but you never know what [software] you’re going to be able to use or not use, or if you’re gonna
have to jump some hurdles just because you’re in this gigantic enterprise environment. Usually
I still need to add a day or two to whatever I have planned, because of unforeseen things. I’ve
gotten better at it, but it’s been challenging." —P14
To counter these barriers, developers turned to structured collaboration through copresence, often combining body doubling with Pomodoro-styled time cycles [16]. These structured intervals provided external
time management while reducing ADHD-specific cognitive fatigue and cognitive load [95]. Specifically,
shared breaks allowed developers to mentally distance themselves from complex problems or cognitively
overwhelming tasks. P14 described how their daily usage of body doubling with a family member through
Pomodoro techniques allowed them to cognitively rest:
"My sister and I use Pomodoro, so it’s basically the 25 minutes and the 5-minute break. In the
5-minute break, it’s usually catching up on "Oh, how was it?" It clears up the brain from what
you’re doing, so you’re not still thinking about the problem that you’re solving while you’re on
break." —P14
Participants also distinguished between physical and virtual closeness. While ad-hoc, in-person sessions
were preferred for social-emotional support, participants favored remote, timed sessions when prioritizing
task productivity and code quality. P5 used remote body doubling via synchronized Pomodoro schedules,
where both partners wore headphones during quiet focus blocks and restricted conversation strictly to
shared breaks.
While body doubling provides a baseline of accountability when partners perform different tasks, our
participants utilized pair programming as a more intensive form of external executive function support for
complex, cognitively demanding tasks. Unlike body doubling, where participants work on separate tasks,
pair programming involves a high degree of mutual behavior where a partner’s actions directly influence
the developer’s next step. Participants (P1, P2, P3, P4, P5, P8, P9, P10, P11, P13, P14) emphasized that partners

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

11

should explicitly align and make a concrete, shared plan together before typing any code, establishing clear
guardrails for the session or sharing a single monitor in person to force mutual attention on a single line of
code at a time. P3 executed pair programming sessions around structured plans: screen-sharing to code
in small blocks, discussing each iteration, and updating documentation together to reinforce learning and
maintain clear guardrails.
By splitting the system knowledge with a partner, participants are able to focus on specific code changes
without losing track of the larger architecture in their codebase. To mitigate distractions that often occur
when passively observing another individual’s work, participants utilized a swapping strategy. By first
investigating separate modules of a complex system independently, the developer pair could then act as
guides for one another. P2 described this swapping technique as a way to maintain active engagement and
manage the cognitive load of a new codebase:
"[We] spend some time separately learning the system, and then pair program a change together.
He [my partner] knew half of the system, I knew the other half. I’d pair program and watch
him do his changes, and then we can swap in and out." —P2
4.1.2 Motivational mechanisms. Participant engagement in copresence was primarily driven by collective
momentum, externalized accountability, and real-time verbal validation.
Participants drew baseline motivation from the concept of mutual behavior, engaging in independent
tasks alongside others in a shared environment. Consistent with previous literature on body double for
individuals with ADHD [4, 23, 24], simply observing peers or strangers working productively (e.g. in coffee
shops or shared remote calls) transformed isolated, daunting tasks into a seemed shared effort. This is
particularly relevant for remote workers, where P1 and P2 work primarily remotely and frequently body
double with friends or strangers in coffee shops. P2 describes how simply knowing that others around them
are also being productive is helpful for task initiation:
"Working remote, sometimes I’m at my desk alone and it kind of sucks. So I would go to coffee
shops or a couple other friends who work remote will get together. And just working in a spot
where you know other people are working does help. I just have a feeling they’re doing something
too." —P2
This ambient presence created a sense of social pressure that lowered the threshold for task initiation
and helped sustain focus without requiring direct interaction.
Beyond motivation, our participants also expressed that body doubling provided externalized accountability. Participants define the practice as two people trying to keep each other accountable while working
on their own task, relying on the presence of a peer to maintain focus on complex tasks. During set focus
time, participants wanted body doubling partners who would check-in on them or offer task support when

12

Pimenova et al.

needed. These focus sessions fulfill the mutual emotion component of copresence by providing socialemotional support through check-ins and structured breaks. P5 noted the balance between productivity
and well-being gained from social interaction:
"I associate it [body doubling] with productivity and I don’t associate it with anything negative.
I think [it is] accountability, and then also during breaks, like, being able to talk to friends. I
think it is a very nice break. So mainly those two aspects." —P5
Participants such as P8 also noted that while social interaction with their copresence partner provided
social-emotional support, it should be time-bound through Pomodoro-style timers (as mentioned in §4.1.1).
Without strict timing, social interaction could create disruption and decrease productivity of a copresence
session.
Finally, when participants shifted from passive body doubling to active collaboration (e.g. pair programming), the motivational mechanism evolved from accountability to cognitive validation. P2 noted that
while they occasionally lose focus during passive observation, being an active participant in a discussion
provided social accountability needed to stay engaged. By externalizing their thought process to a partner,
participants move from a state of internal confusion to active problem-solving. P2 and P3 both described
how pair programming also provides validation through real-time verbal feedback that reduces performance
anxiety and catches obvious mistakes they may have missed on their own.
4.1.3 Interpersonal partner dynamics. The interpersonal success of a copresence session is heavily dependent
on the underlying relationship dynamics. Participants emphasized that effective collaboration required
psychological safety and a sense of mutual respect, which increased satisfaction and well-being during
collaboration. Conversely, a lack of trust or safety heightened performance anxiety and reduced satisfaction.
P8 describes comfort with engaging in focus sessions with a partner they trust:
"Whether I can focus largely depends on the person I’m with. Co-workers that I like to be around,
and that I trust to actually have good input keep me on task. People who I trust more and respect
their abilities more, it’s easier for us to collaborate." —P8
While some developers accepted strangers for passive body doubling, most preferred familiar partners who
could balance quiet focus blocks with friendly conversation and check-ins during breaks for social-emotional
support. P2 noted that an ideal partner should be sociable and non-threatening:
"I guess someone having knowledge in the area is nice, if I do really hit a point I’m stuck, I can
just quickly talk to them about it. It would be really weird if they’re antagonistic to me. That
just freaks me out." —P2
When selecting a pair programming partner, developers intentionally sought individuals with different
or complementary skills. Partnering with a more experienced peer with complementary skills allowed
participants to overcome task-initiation hurdles and maintain a consistent mental model of complex
codebases. For example, P3 compared their pair programming sessions to an "apprenticeship" that enabled

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

13

them to learn complex systems by active participation rather than reading passive documentation. P9
described how complementary skills assisted with learning during pair programming:
"Pair programming was helpful as a learning tool. It is the equivalent of having an LLM trying
to fix your code with you instead of fixing it for you. So it was helpful as somebody who’s new
and trying to learn. My partner had the expertise to know where to put stuff, and I knew what
needed to be put in there, so it felt complementary." —P9
4.2

Challenges and Mitigation Strategies of Current Copresence Practices

While copresence offers essential structural support for developers with ADHD, it also introduces performance anxiety (§4.2.1), disrupts flow state when executed poorly (§4.2.2), and does not account for
company-related privacy constraints (§4.2.3).
4.2.1 Performance Anxiety. Even before collaboration begins, executive dysfunction and emotional task
avoidance raise barriers to task initiation, creating challenges around scheduling, planning, and interpersonal
coordination required to initiate a copresence session. P6 described wanting to utilize body doubling, but
routinely struggled to initiate sessions due to internalized anxiety–a sentiment echoed by P12 who valued
body doubling but hesitated to reach out to their peers:
"I like the other members of my team, but I don’t want them to watch me work or bother them. I
think it goes back to when I was young, and I had a feeling that I wasn’t doing things the way
I was supposed to do them and a feeling that other people are watching me, that I’m kind of
doing things wrong in some way. It’s quite deep." —P12
This fear of observation extends into live collaboration and is heightened by the need of participants to
maintain a professional persons around colleagues. This dynamic created two challenges: it made initiating
body doubling sessions intimidating, and once in a session, an internalized fear of asking clarifying questions
hindered active problem-solving. P13 described how overcoming this anxiety to ask clarifying questions is
vital for preventing systemic mistakes. Framing partner pairings as a reciprocal, problem-focused partnership
can help decrease performance anxiety.
4.2.2 Disruption to Flow State. Beyond emotional overhead, real-time collaboration presents distinct
cognitive challenges for our participants. An example is when partners are not synchronized in focus, which
can create distractions. P6 described this as a lack of "harmonic co-working." For developers who are in a
state of hyperfocus, live pair programming on smaller tasks can disrupt their internal map of the codebase,
where P10 only wanted ambient music over human presence for deep focus:
"I wouldn’t use pair programming for any deep coding that I need to be in a flow state for. The
only distraction I could have is minimal music." —P10
Unpredictable workplace interruptions also disrupt flow, where P5 and P1 noted avoiding copresence
altogether during on-call periods due to the guilt of disturbing partners or losing momentum during sudden

14

Pimenova et al.

context shifts. P1 explained how unscheduled calls prevent them from participating in copresence practices
alltogether:
"It’s very common to get calls out of the blue. You could be working on something for 3 hours,
then all of a sudden, boom, get a call with a new thing, forget everything from before. I like to
go and body double in public, but then I don’t know when I’m gonna take a call. I don’t want to
distract others and I don’t want to lose my own focus." —P1
4.2.3 Privacy Constraints. Finally, the transition to remote collaboration introduces structural trade-offs
between security policies and executive function support. P6 and P9 emphasized that corporate NDAs and
data privacy regulations severely restrict traditional screen-sharing practices. Our participants relied on
screen sharing during body doubling and pair programming sessions for visual accountability, where they
would risk sharing sensitive information to outsiders or feel a sense of heightened anxiety when screen
sharing with coworkers. P6 described the need for a privacy-preserving alternative towards screen-sharing
during copresence sessions:
"Sometimes I am just browsing information and accidentally lose control [of my focus], but I
don’t want to share my full screen in front of everyone. I’m wondering if there is a design that
could simulate in-person collaboration such as a neighbor who can see my screen, but cannot see
what exactly I am doing. That way of accountability would be more helpful and private." —P6
4.3

The Role of AI in Copresence

While participants were largely open to AI as a copresence partner, they expressed nuanced perspectives
regarding how AI can enhance productivity, where it falls short, and how it compares to human interaction.
We describe how AI supports flow state (§4.3.1), human boundaries in AI-mediated copresence (§4.3.2), and
social-emotional support (§4.3.3).
4.3.1 AI Supports Flow State. The usage of agentic coding tools (predominantly Claude Code and GitHub
Copilot) was frequent and widespread, where all participants had experience with AI for programming and
most participants (P1, P3, P5, P6, P7, P8, P9, P10, P12, P13) had positive perceptions. Out of participants who
had negative perceptions (P2, P4, P11, P14), only one participant (P11) completely avoided AI use. Generally,
participants with positive perception of AI characterized the AI tools as pair programming partners, who
could create uninterrupted, long periods of flow state. P5 describes:
"It’s almost like a honeymoon and I actually cannot see any project that I would not want to
use it for. Ironically, I probably have more positive feelings towards pair programming with
an AI than with a human... because unlike a human, [the AI] doesn’t interrupt my flow with
unrelated small talk that distracts or hinders moving forward." —P5
Further, agentic AI workflows support multi-stream execution, allowing developers to manage parallel
streams of problem-solving across interfaces without losing cognitive context. For instance, P10 described

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

15

rapidly orchestrating work across terminals, notes, GitHub, and local code bases, leveraging concurrent AI
agents to maintain momentum without getting overwhelmed in context switching:
"I have two different terminal apps. I just opened Claude inside of the terminal, then I’ll have,
Obsidian. I’ll have my codebase, in Finder next to it, and I’ll have another tab open with GitHub
and another one open with my notes. And then I’ll jump back and forth and I might open up
a new agent. A lot of orchestrating things because it’s a lot faster and each stream of thought
updates based on what you’re reading from each tab. It’s actually kind of goated." —P10
AI-based tools also offload additional workload by digesting large amounts of documentation and
providing code validation in real time. Rather than relying on AI to write end-to-end solutions, participants
often used AI to establish high-level skeletons before stepping in to review and refine the output. For
instance, P7 used AI agents to summarize complex codebases and generate initial structural frameworks,
allowing human effort only for auditing output. By continuously prompting developers for clarification
and providing task summaries, the AI tools forced developers to externalize, articulate, and organize their
thought processes.
4.3.2 Human boundaries for AI copresence. Despite the AI-mediated copresence providing support with
entering flow state, our participants drew boundaries where human support is still needed. When code
validation or domain expertise is required for complex or sensitive projects, developers experience heightened accountability-based anxiety. Due to AI tools bearing no systemic accountability, using an AI tool
as a copresence partner (particularly for pair programming) shifts cognitive burden of auditing code and
searching for errors onto the individual developer. To mitigate this stress, participants prioritized human
copresence for trusted code verification. P5 noted:
"I actually really like working with AI agents, but in terms of human pair programming, a really
good use case would be where the other person has more expertise than I do with a particular
thing or where I genuinely cannot tell if the code I’ve written is accomplishing the conceptual
task. In those scenarios, it’s very helpful to have someone [a human] there for verification." —P5
This boundary becomes especially pronounced in sensitive projects or high-stakes production environments, where participants described the process of manually auditing large volumed of AI code increases
cognitive exhaustion and anxiety over hidden bugs. P11 emphasized that using AI for pair programming
without human verification created individual cognitive burden:
"Infrastructure and production stuff never gets generated for me. You can’t afford a failure in
these mission-critical systems. It kind of turns into spaghetti after a couple weeks. Everyone’s
like, "Oh, but I can do this with Claude in two hours." I’m like, yes, but can you maintain it?
Can you scale it? Then if it doesn’t work it’s all on me." —P11
Similarly, P10 explained that without high-level architectural oversight, rapid AI code generation risks
optimizing execution speed at the expense of strategic direction:

16

Pimenova et al.
"I use the analogy where you’re in super-fast car... This is AI agents, you have no bird’s eye view
to tell you if you’re going the right way. A human would ask you, ’Why are you going this
way?’" —P10
Further, when human-human copresence sessions include both partners using individual AI tools, rapid

and unannounced AI usage by one partner can hinder the pair’s shared mental model. In these hybrid
sessions, participants expressed cognitive overload when a partner offloaded work to AI agents in real time
without transparent communication. This challenge highlights how unaligned AI usage disrupts mutual
attention–when one developer independently prompts an AI without keeping their partner informed. P14
detailed this breakdown:
"It ended up being pair-programming without us actually wanting it to be. Mostly it was [my
partner] telling Claude a bunch of stuff, and Claude doing a bunch of stuff, and me saying,
"What is happening?" It was stressing, because I was trying to keep up with what the AI is doing
and also you have the other person that is quickly changing screens." —P14
4.3.3 Social-emotional support. A central trade-off in AI-mediated copresence sessions involves balancing
social accountability with authentic emotional support. Our participants noted that when AI acts as a
copresence partner, performance anxiety related to human observation is lowered. However, participants
described how AI tools lack social support and emotional connection, meaning AI-based copresence lacks a
sense of mutual emotion.3 P2 explained how simulated social interactions with AI do not provide socialemotional support, as AI agents lack human emotion:
"I don’t feel like an AI gets bored. I can relate to someone around me who’s just like, you know
what, I need a break for a minute. Let’s talk or something. If an AI did it, it’s clearly doing it
just to placate me." —P2
In some cases, the absence of human emotional traits can increase a developer’s productivity. An AI-based
copresence partner offers a predictable and controllable environment, allowing developers to enter flow
state without social anxiety. P10 explains how social and emotional support are less important for success
in their role, where they primarily aim to increase their everyday productivity:
"I think the social or emotional support are less relevant. I think people or friends should follow
that purpose. I think [for AI] productivity is better. If you have a set of tasks that are automatable,
just ask an AI to write a script for you. I don’t want to befriend it." —P10
Additionally, AI-based copresence partners can assist with structuring routine breaks that alleviate
cognitive load. Beyond executing technical tasks, agents can simulate light, human-like check-ins which
provide visual and temporal transitions during focus periods. P6 explains how an AI tool could mimic
human interaction through check-ins:
3 Mutual emotion is a core component of copresence theory [14].

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

17

"If [An AI] periodically checks in whether I need to take a break and grab a coffee sounds more
human. Sometimes when [a human colleague] checks in on me, that 5-minute talk is really
helpful for stress relief." —P6
While our participants generally recognized that current AI agents couldn’t fulfill the social-emotional
support gained from human interaction, some participants either didn’t want human interaction during
focus periods, or have suggestions for how AI tools could seem more human. This shows potential for the
development of AI tools that could act as copresence partners, which we discuss in §5.3.
5

Discussion

Fig. 3. Flow of ADHD characteristics and barriers mitigated by copresence practices (body doubling, pair
programming) that then impact aspects of developer productivity

We synthesize our empirical findings to answer our three primary research questions through theoretical
implications in §5.1, implications for developer productivity in §5.2, and design implications for future
copresence tools in §5.3. Regarding our first research question (RQ1) on how software engineers with ADHD
engage in copresence, we find that while collaborative practices like pair programming broadly benefit
software engineers, copresence specifically functions as assistive support to mitigate executive dysfunction
for developers with ADHD. Addressing our second research question (RQ2) on challenges and strategies of
copresence practices, we extend prior CSCW literature that treats copresence primarily through physical
or virtual proximity [33, 37, 43, 49, 72, 85] through interviews of 14 developers with ADHD navigating
trade-offs between cognitive support and workplace barriers. Finally, to answer our third research question
(RQ3) on designing AI-assisted copresence, we provide design implications and theoretical extensions
across §5.1, §5.2, and §5.3.
5.1

Theoretical Implications Related to ADHD

Our findings align with and build on aspects of copresence theory, including mutual attention, mutual
behavior, and mutual emotion. Mutual attention requires two or more actors to maintain direct, reciprocal
focus on one another [14]. This typically relies on continuous visual or auditory signals, such as open

18

Pimenova et al.

cameras and unmuted microphones in remote settings or physical proximity in shared workspaces [72].
However, our findings show that for developers with ADHD, continuous monitoring often triggers job
performance-related anxiety and a state of hypervigilance. Based on our findings, we propose ambient
mutual attention, where developers can achieve a sense of mutual attention through low-fidelity, ambient
signals such as soft background chatter or passive status widgets within an IDE. These ambient cues provide
a sense of shared presence to help developers initiate and sustain task focus without overwhelming working
memory or forcing defensive impression management across copresent peers [47].
Copresence theory describes mutual behavior as the notion of two individuals who mimic each other’s
behavior [14]. We find that developers with ADHD feel more motivated to initiate a task or continue making
progress toward a task when their partner is also initiating or making progress on a work-related task.
We also find a distinction between parallel mutual behavior (body doubling) and joint mutual behavior
(pair programming). In parallel mutual behavior, each individual is less concerned about the nature of the
other person’s task, where joint mutual behavior requires cognitive alignment between the developers
to be successful in making progress toward task completion. Joint mutual behavior requires transparent
communication and documentation, which AI-based tools can increase the speed of. This communication
shifts interactions from surface-level I-Awareness (knowing what a partner is doing) to We-Awareness
(establishing shared reasoning and intentionality) [84]. By automatically externalizing code rationale and
summaries, AI tools help sustain this We-Awareness without overloading the working memory of developers
with ADHD.
Finally, mutual emotion refers to shared affective states, empathy, and emotional alignment between
actors [14]. This aspect relies heavily on shared physiological responses and mutual emotional mirroring.
Our findings demonstrate that developers with ADHD value mutual emotion primarily as a source of socialemotional support and validation during structured breaks or downtime, rather than during active code
execution. Importantly, we observe a contrast in how mutual emotion operates across human-human and
human-AI interactions. While human partners provide empathy and support, they also introduce perceived
social judgment. Conversely, AI copresence partners completely lack emotional judgment, boredom, or
social expectations. A lack of mutual emotion creates a sense of psychological safety by allowing developers
to make mistakes, ask basic questions, or pause work without experiencing social shame or evaluative
anxiety.
5.2

Implications for Developer Productivity

To examine how copresence practices influence the productivity of developers with ADHD, we analyze our
findings through the SPACE framework of developer productivity [30]. The SPACE framework measures
developer productivity within five key dimensions of Satisfaction, Performance, Activity, Communication,
and Efficiency. The framework was developed across the fields of human-computer interaction, software
engineering, and organizational psychology [30]. Our analysis focuses specifically on Satisfaction and

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

19

Well-being, Communication and Collaboration, and Efficiency and Flow, which are represented the most
within our empirical findings.
Within the SPACE framework, Satisfaction and Well-being refer to the levels of happiness, fulfillment,
and psychological safety developers experience while completing tasks and interacting with their environment [30]. Current professional settings often overlook emotional labor and exhaustion (i.e. invisible access
labor [38, 91]) experienced by developers with ADHD. We find that executive dysfunction of developers
with ADHD can lead to task avoidance, internalized shame, and fear of falling behind. While copresence
practices generally improve job satisfaction by providing social connection and accountability, certain scenarios where a developer has different knowledge or experiences from their partner (e.g. a junior developer
paired with a senior developer) could increase performance anxiety and thus decrease overall satisfaction
and well-being. The Zone of Proximal Development (ZPD) describes the gap between what a learner can
accomplish independently and what they can achieve with guidance from a more capable partner [2, 15, 17],
when a senior developer navigates at their own fluency level, they push the interaction well beyond the
junior developer’s ZPD, lessening the space where learning can occur. Thus, strategies such as thorough
on-boarding, workplace boundary setting, consistent documentation, or AI-based copresence can contribute
to non-judgmental copresense sessions which allow all developers with ADHD to experience the benefits
of copresence practices.
Furthermore, the SPACE framework describes Communication and Collaboration as the quality and
effectiveness of information sharing, coordination, and teamwork between developers of a team or teams
through a shared mental model [30]. We find that developers with ADHD experience friction in traditional
synchronous collaboration and communication due to environmental barriers such as unclear requirements,
unwritten social norms, or non-dynamic meeting hours. This is particularly relevant in AI-assisted development, where Storey introduces intent debt, the loss of explicit rationale and goals, and cognitive debt, which
erodes shared mental models across developers. In human-human copresence sessions where each human
is using AI, rapid code generation by one partner without real-time explanation hinders context and lessens
communication and collaboration between developers, increasing the risk of intent debt [82].
Finally, Efficiency and Flow in the SPACE framework capture a developer’s ability to maintain focus,
minimize friction, and sustain momentum without incurring severe cognitive fatigue [30]. For developers
with ADHD, the flow state (hyperfocus) [35, 39, 68] is a strength that allows them to spend extended periods
on difficult or cognitively challenging tasks. When developers enter a flow state, they reach total immersion
of a particular concept and thus are able to be efficient, productive, and tend to experience a sense of
enjoyment [13, 60]. However, environmental barriers such as unpredictable workplace interruptions, rigid
time-tracking constraints, or latency during AI generation frequently disrupt this state, making context
recovery more difficult. Developers with ADHD are able to reach flow state within body doubling and pair
programming practices, but certain modalities of these practices (e.g. partner experience or personality
mismatch described in §4.1.3) increase burnout and risk the accumulation of cognitive debt [82]. Ultimately,

20

Pimenova et al.
Table 2. Mapping of design implications to empirical findings and copresence theory
Design Implication
𝐷 1 : Tools could assist with finding
copresence partners and automating
session initiation to alleviate activation
anxiety and fear of interrupting peers
𝐷 2 : Tools could provide periodic, ambient
check-ins by posing contextually related
follow-up questions during task execution,
reinforcing accountability without
inducing evaluative surveillance or
micromanagement.
𝐷 3 : Tools could shift from clock-based
break timers to activity-based dynamic
timers through AI prediction of context
switching and generation latency, where
both partners could have mutual breaks
during wait periods.

Empirical Finding
Developers desire copresence
but experience initiation anxiety,
internalized shame, and fear of
interrupting peers (§4.2.1).
Developers want to participate
in copresence practices with a
human or AI partner who
occasionally checks in on them,
but without constant
surveillance (§4.1.2).
Rigid, clock-based timers and
wait periods from AI generation
latency disrupt flow and
hyperfocus (§4.1.1, §4.3.2)

Copresence Theory
Mutual Attention,
Mutual Behavior

Mutual Attention,
Mutual Behavior

Mutual Emotion,
Mutual Behavior

we find that a combination of human-human body doubling and human-AI pair programming structures
optimize efficiency and flow.
5.3

Design Implications for Copresence Technology

Translating our empirical findings into actionable implications for systems, we propose three core design
implications (𝐷 1 –𝐷 3 ) to facilitate human-human body doubling and human-AI copresence practices for
software engineers with ADHD. Each recommendation directly targets a specific phase of task execution: task
initiation (§5.3.1), maintenance of flow (§5.3.2), and task completion (§5.3.3). We map these recommendations
to our empirical findings and core dimensions of copresence theory in Table 2.
5.3.1 Task Initiation (𝐷 1 ). We find that developers desire copresence sessions, but experience barriers such
as initiation anxiety, internalized shame, and fear of interrupting peer workflows with manual outreach.
Copresence tools could support task initiation by automating session setup (𝐷 1 ). Instead of relying on static
scheduling, tools could incorporate dynamic, context-aware matching algorithms inspired by peer-study and
collaborative platforms [71, 86]. Future partner matching algorithms could use criteria including task type,
estimated time of task completion, IDE activity states, and more to asynchronously pair developers with
partners working towards similar goals. This matching process could provide a sense of mutual behavior
and the automation of task initiation could alleviate the social anxiety our participants expressed when
reaching out to peers. However, Viduchinsky described how individuals can feel compelled to perform for
the algorithm, which can be different from their own identity [90]. Future copresence tools should continue
to support user agency and well-being in the matching process through matching by qualities of task rather
than qualities of the individual developer.

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

21

5.3.2 Maintenance of Flow (𝐷 2 ). Maintaining flow for developers with ADHD is disrupted by context
switching, AI generation wait periods, and the cognitive overload of mismatching partner expertise. To
lessen internal distractions without inducing performance anxiety, future copresence tools could use
non-intrusive social contract reminders such as private, gentle check-ins—to reinforce accountability
when developers stray off task. This could be similar to Lee et al.’s "Surrogate Avatar" which dynamically
adapts its positioning in the background using a distributed optimization framework to balance realtime responsiveness with computational efficiency, ensuring presence without disrupting flow [49]. In
pairing with mismatched experiences (e.g. junior and senior developer pairs), AI-based tools could provide
background summaries and automated documentation (similar to Zoom’s AI note taker [99]) to support
junior developer’s learning and understanding without requiring senior developers to spend additional
time on note taking and documentation.
5.3.3 Task Completion and Breaks (𝐷 3 ). We find that clock-based timers with rigid schedules and wait
periods from AI generation disrupt developer’s flow and states of hyperfocus. However, identifying optimal
opportunities for systems to dynamically recommend breaks was constrained by the inability to predict task
boundaries or context switches. As the developer’s role shifts from active coding to monitoring AI agents and
managing AI-led task decomposition, predicting these state transitions to dynamically schedule contextual
breaks becomes increasingly feasible. Future copresence technology could replace existing rigid timers
with dynamic, ambient timers on automated, synchronized break schedules. This could be an extension of
existing timer-based focus tools such as the Flow app or FocusMate [27, 28, 52]. Kwa et al. demonstrated that
while short-level inference latency of AI agents is increasingly predictable, recent benchmark evaluations
demonstrate that state-of-the-art AI agents have highly variable execution time horizons [46]. Our findings
suggest that predicting AI generation wait times could mitigate workflow pauses, and future copresence
tools could synchronize these wait times through dynamic breaks. Future tools could deploy break prompts,
where both partners can agree to initiate a break, where the tool could then automatically unmute audio
and camera streams and provide suggestions for shared discussion prompts. This structures necessary
social and emotional support periods while reducing social anxiety surrounding conversation initiation. By
supporting transitions into social-emotional breaks, future tools could assist with preventing developer
burnout.
5.4

Limitations

Our findings reflect semi-structured interviews with 14 software developers with ADHD, focusing on their
lived experiences with copresence practices and AI-assisted collaboration. Software engineers with ADHD
represent an understudied and difficult-to-reach population in HCI research due to corporate non-disclosure
agreements, privacy concerns surrounding ADHD disclosure, and high compensation levels that make
research participation difficult to incentivize. Although our sample included both early-career and senior
developers in different workplace settings (e.g. hybrid, remote, in-person) our findings may not fully capture

22

Pimenova et al.

the strategies of all developers with ADHD. Additionally, while our sample included diverse gender identities,
larger demographic samples are needed to analyze gendered dimensions in depth. Despite these recruitment
constraints, our qualitative sample achieved thematic saturation across extensive transcript data. While
our objective was deep empirical understanding rather than statistical generalization, future work should
evaluate copresence practices across larger sample sizes in varying settings.
6

Conclusion

In this paper, we investigate how software engineers with ADHD navigate, adapt to, and benefit from
copresence practices including body doubling, pair programming, and agentic human-AI co-creation within
modern hybrid workplace settings. Through semi-structured interviews with 14 software engineers with
ADHD, we describe how environmental barriers and factors such as performance anxiety impact executive
function, focus, and overall developer productivity. By grounding our empirical findings in copresence
theory and the SPACE framework of developer productivity, we discuss how non-evaluative, AI-based
tools can mitigate social anxiety, preserve shared mental models, and reduce cognitive load without
disrupting developer flow. Ultimately, our findings reveal that copresence is not a one-size-fits-all construct,
as developers with ADHD thrive when supported by flexible, ambient, and non-judgmental methods of
collaboration. By translating these insights into design implications for future agentic copresence technology,
we hope to inspire collaborative systems that foster a more inclusive and accessible software engineering
workplace that expands beyond neurotypical abilities.
References
[1] ADDA Editorial Team. 2025. The ADHD Body Double: A Unique Tool for Getting Things Done. Attention Deficit Disorder
Association (ADDA) Library. https://pubmed.ncbi.nlm.nih.gov/33427949/
[2] Nicole Anderson and Tim Gegg-Harrison. 2013. Learning computer science in the "comfort zone of proximal development".
In Proceedings of the 44th ACM technical symposium on Computer science education (SIGCSE ’13). Association for Computing
Machinery, New York, NY, USA, 495–500. doi:10.1145/2445196.2445344
[3] Erik Arisholm, Hans Gallis, Tore Dyba, and Dag I.K. Sjoberg. 2007. Evaluating Pair Programming with Respect to System
Complexity and Programmer Expertise. IEEE Transactions on Software Engineering 33, 2 (2007), 65–86. doi:10.1109/TSE.2007.17
[4] Vitica X Arnold, Aehong Min, Clarisse Bonang, Sohyeon Park, Gillian R Hayes, and Anne Marie Piper. 2025. Beyond Individual
Accommodations: The Collaborative Practices of ADHD Students in Post-Secondary Education. In Proceedings of the 27th
International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS ’25). Association for Computing Machinery,
New York, NY, USA, Article 36, 14 pages. doi:10.1145/3663547.3746324
[5] Julia Bachmann, Adam Zabicki, Stefan Gradl, Johannes Kurz, Jörn Munzert, Nikolaus F. Troje, and Britta Krueger. 2021. Does
co-presence affect the way we perceive and respond to emotional interactions? Experimental Brain Research 239, 3 (Mar 2021),
1011–1023. doi:10.1007/s00221-020-06020-5
[6] Philip Baillargeon, Jina Yoon, and Amy Zhang. 2025. Who Puts the "Social" in "Social Computing"?: Using A Neurodiversity
Framing to Review Social Computing Research. Proc. ACM Hum.-Comput. Interact. 9, 2, Article CSCW208 (May 2025), 44 pages.
doi:10.1145/3711106
[7] Russell A. Barkley, Kevin R. Murphy, and Mariellen Fischer. 2008. ADHD in Adults: What the Science Says. Guilford Press, New
York, NY.

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

23

[8] Colin Barnes. 2019. Understanding the social model of disability: Past, present and future. In Routledge Handbook of Disability
Studies (2nd ed.), Nick Watson and Tom Shakespeare (Eds.). Routledge, London, 14–31. doi:10.4324/9780429430817-2
[9] Andrew Begel and Nachiappan Nagappan. 2008. Pair programming: what’s in it for me?. In Proceedings of the Second ACM-IEEE
International Symposium on Empirical Software Engineering and Measurement (Kaiserslautern, Germany) (ESEM ’08). Association
for Computing Machinery, New York, NY, USA, 120–128. doi:10.1145/1414004.1414026
[10] Nathalie Boot, Barbara Nevicka, and Matthijs Baas. 2020. Creativity in ADHD: Goal-directed motivation and domain specificity.
Journal of Attention Disorders 24, 13 (2020), 1857–1866. doi:10.1177/1087054717727352
[11] Sydnie Born. 2024. The Effects of Accountability and Body Doubling on Productivity for People With Attention Deficits. Master’s
thesis. Lamar University - Beaumont.
[12] Stacy M. Branham and Shaun K. Kane. 2015. The Invisible Work of Accessibility: How Blind Employees Manage Accessibility in
Mixed-Ability Workplaces. In Proceedings of the 17th International ACM SIGACCESS Conference on Computers & Accessibility
(ASSETS ’15). ACM, New York, NY, USA, 163–171. doi:10.1145/2700648.2809864
[13] Pedro Calais and Lissa Franzini. 2023. Test-Driven Development Benefits Beyond Design Quality: Flow State and Developer
Experience. In 2023 IEEE/ACM 45th International Conference on Software Engineering: New Ideas and Emerging Results (ICSE-NIER).
106–111. doi:10.1109/ICSE-NIER58687.2023.00025
[14] Celeste Campos-Castillo and Steven Hitlin. 2013. Copresence: Revisiting a Building Block for Social Interaction Theories.
Sociological Theory 31, 2 (2013), 168–192. doi:10.1177/0735275113489811
[15] Seth Chaiklin. 2003. The Zone of Proximal Development in Vygotsky’s Analysis of Learning and Instruction. In Vygotsky’s
Educational Theory in Cultural Context, Alex Kozulin, Boris Gindis, Vladimir S. Ageyev, and Suzanne M. Miller (Eds.). Cambridge
University Press, Cambridge, UK, 39–64. doi:10.1017/CBO9780511840975.004
[16] Francesco Cirillo. 2018. The Pomodoro technique: The acclaimed time-management system that has transformed how we work.
Crown Currency.
[17] Michael Cole and SYLVIA SCRIBNER. 1978. Vygotsky, lev s.(1978): Mind in society. the development of higher psychological
processes.
[18] Maitraye Das, John Tang, Kathryn E. Ringland, and Anne Marie Piper. 2021. Towards Accessible Remote Work: Understanding
Work-from-Home Practices of Neurodivergent Professionals. Proc. ACM Hum.-Comput. Interact. 5, CSCW1, Article 183 (April
2021), 30 pages. doi:10.1145/3449282
[19] David Deming and OpenAI Economic Research. 2025. How people are using ChatGPT. Working Paper. National Bureau of
Economic Research (NBER). https://openai.com/index/how-people-are-using-chatgpt/
[20] Nicole M. Deterding and Mary C. Waters. 2021. Flexible Coding of In-depth Interviews: A Twenty-first-century Approach.
Sociological Methods & Research 50, 2 (2021), 708–739. doi:10.1177/0049124118799377
[21] Kezia Devathasan, Nowshin Nawar Arony, Emerson Murphy-Hill, and Daniela Damian. 2025. Empathy, self-determination and
motivation: moderating diversity for enhanced performance in software development teams. Empirical Software Engineering 30,
82 (2025). doi:10.1007/s10664-025-10632-2
[22] Melanie Duckert and Pernille Bjørn. 2025. Location Multiplicity: Lost Space in the Hybrid Office. Proc. ACM Hum.-Comput.
Interact. 9, 2, Article CSCW126 (May 2025), 25 pages. doi:10.1145/3711024
[23] Tessa Eagle, Leya Breanna Baltaxe-Admony, and Kathryn E. Ringland. 2023. Proposing Body Doubling as a Continuum of
Space/Time and Mutuality: An Investigation with Neurodivergent Participants. In Proceedings of the 25th International ACM
SIGACCESS Conference on Computers and Accessibility (New York, NY, USA) (ASSETS ’23). Association for Computing Machinery,
New York, NY, USA, Article 85, 4 pages. doi:10.1145/3597638.3614486
[24] Tessa Eagle, Leya Breanna Baltaxe-Admony, and Kathryn E. Ringland. 2024. “It Was Something I Naturally Found Worked and
Heard About Later”: An Investigation of Body Doubling with Neurodivergent Participants. ACM Trans. Access. Comput. 17, 3,
Article 16 (Oct. 2024), 30 pages. doi:10.1145/3689648

24

Pimenova et al.

[25] Mikhail Evtikhiev, Ekaterina Koshchenko, and Vladimir Kovalenko. 2025. What Could Possibly Go Wrong: Undesirable Patterns
in Collective Development. ACM Transactions on Software Engineering and Methodology 34, 3 (2025). doi:10.1145/3707451
[26] Paul Ezeamii and Kristen Shinohara. 2025. Navigating STEM Doctoral Programs with ADHD: Barriers, Workflow Challenges,
and Adaptive Strategies. In Proceedings of the 27th International ACM SIGACCESS Conference on Computers and Accessibility
(ASSETS ’25). Association for Computing Machinery, New York, NY, USA, Article 38, 13 pages. doi:10.1145/3663547.3746325
[27] Flow. 2026. Flow: Focus & Pomodoro Timer. https://www.flow.app/
[28] Focusmate Inc. [n. d.]. Focusmate: Virtual Body Doubling for Getting Anything Done. https://www.focusmate.com/
[29] Denae Ford, Margaret-Anne Storey, Thomas Zimmermann, Christian Bird, Sonia Jaffe, Chandra Maddila, Jenna L. Butler, Brian
Houck, and Nachiappan Nagappan. 2021. A Tale of Two Cities: Software Developers Working from Home during the COVID-19
Pandemic. ACM Trans. Softw. Eng. Methodol. 31, 2, Article 27 (Dec. 2021), 37 pages. doi:10.1145/3487567
[30] Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, and Jenna Butler. 2021. The
SPACE of developer productivity. Commun. ACM 64, 6 (May 2021), 46–53. doi:10.1145/3453928
[31] A. B. M. Fuermaier, L. Tucha, M. Butzbach, M. Weisbrod, S. Aschenbrenner, and O. Tucha. 2021. ADHD at the workplace:
ADHD symptoms, diagnostic status, and work-related functioning. Journal of Neural Transmission 128, 7 (Jul 2021), 1021–1031.
doi:10.1007/s00702-021-02309-z
[32] Kiev Gama and Aline Lacerda. 2023. Understanding and Supporting Neurodiverse Software Developers in Agile Teams. In
Proceedings of the XXXVII Brazilian Symposium on Software Engineering (Campo Grande, Brazil) (SBES ’23). Association for
Computing Machinery, New York, NY, USA, 497–502. doi:10.1145/3613372.3613384
[33] Gernot Goebbels and Vali Lalioti. 2001. Co-presence and co-working in distributed collaborative virtual environments. In
Proceedings of the 1st International Conference on Computer Graphics, Virtual Reality and Visualisation (Camps Bay, Cape Town,
South Africa) (AFRIGRAPH ’01). Association for Computing Machinery, New York, NY, USA, 109–114. doi:10.1145/513867.513891
[34] Erving Goffman. 1963. Behavior in Public Places: Notes on the Social Organization of Gatherings. Free Press of Glencoe, New York.
[35] Joshua Gold and Joseph Ciorciari. 2020. A review on the role of the neuroscience of flow states in the modern world. Behavioral
Sciences 10, 9 (2020), 137.
[36] Dan Goodley, Bill Hughes, and Lennard J. Davis (Eds.). 2012. Disability and Social Theory: New Developments and Directions.
Palgrave Macmillan, London, UK. doi:10.1057/9781137023001
[37] Kate Goodwin, Frank Vetere, and Gregor Kennedy. 2010. Being there with others: copresence and technologies for informal
interaction. In Proceedings of the 22nd Conference of the Computer-Human Interaction Special Interest Group of Australia on
Computer-Human Interaction (Brisbane, Australia) (OZCHI ’10). Association for Computing Machinery, New York, NY, USA,
324–327. doi:10.1145/1952222.1952291
[38] Nicole Gustavsen. 2023. The Invisible Labor of Managing Executive Dysfunction at Work. In Proceedings of the Washington
Library Association 2023 Neurodiversity & Libraries Summit. https://repository.gonzaga.edu/foleyschol/36
[39] David J Harris, Samuel J Vine, and Mark R Wilson. 2017. Neurocognitive mechanisms of the flow state. Progress in brain research
234 (2017), 221–243.
[40] Steffen Holter and Mennatallah El-Assady. 2024. Deconstructing Human-AI Collaboration: Agency, Interaction, and Adaptation.
Computer Graphics Forum 43, 3 (2024), e15107. doi:10.1111/cgf.15107
[41] Kathleen E Hupfeld, Tessa R Abagis, and Priti Shah. 2019. Living “in the zone”: hyperfocus in adult ADHD. ADHD Attention
Deficit and Hyperactivity Disorders 11 (2019), 191–208.
[42] Victoria Jackson, André van der Hoek, and Rafael Prikladnicki. 2022. Collaboration Tool Choices and Use in Remote Software
Teams: Emerging Results from an Ongoing Study. In Proceedings of the 15th International Conference on Cooperative and
Human Aspects of Software Engineering (CHASE ’22). Association for Computing Machinery, New York, NY, USA, 76–80.
doi:10.1145/3528579.3529171
[43] Sin-Hwa Kang, James H. Watt, and Sasi Kanth Ala. 2008. Social copresence in anonymous social interactions using a mobile
video telephone. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Florence, Italy) (CHI ’08).

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

25

Association for Computing Machinery, New York, NY, USA, 1535–1544. doi:10.1145/1357054.1357295
[44] Ronald C. Kessler, Lenard Adler, Minnie Ames, Russell A. Barkley, Howard Birnbaum, Paul Greenberg, Joseph A. Johnston,
Thomas Spencer, and T. Bedirhan Ustün. 2005. The prevalence and effects of adult attention deficit/hyperactivity disorder on
work performance in a nationally representative sample of workers. Journal of Occupational and Environmental Medicine 47, 6
(2005), 565–572. doi:10.1097/01.jom.0000166863.33541.39
[45] Ronald C Kessler, Lenard Adler, Russell Barkley, Joseph Biederman, C Keith Conners, Olga Demler, Stephen V Faraone, Laurence L
Greenhill, Mary J Howes, Kristina Secnik, Thomas Spencer, T Bedirhan Ustun, Ellen E Walters, and Alan M Zaslavsky. 2006.
The prevalence and correlates of adult ADHD in the United States: results from the National Comorbidity Survey Replication.
American Journal of Psychiatry 163, 4 (2006), 716–723. doi:10.1176/ajp.2006.163.4.716 PMID: 16585449.
[46] Thomas Kwa, Ben West, Joel Becker, Amy Deng, Katharyn Garcia, Max Hasin, Sami Jawhar, Megan Kinniment, Nate Rush,
Sydney Von Arx, Ryan Bloom, Thomas Broadley, Haoxing Du, Brian Goodrich, Nikola Jurkovic, Luke Harold Miles, Seraphina
Nix, Tao Lin, Chris Painter, Neev Parikh, David Rein, Lucas Jun Koba Sato, Hjalmar Wijk, Daniel M. Ziegler, Elizabeth Barnes,
and Lawrence Chan. 2026. Measuring AI Ability to Complete Long Software Tasks. arXiv:2503.14499 [cs.AI] https://arxiv.org/
abs/2503.14499
[47] Airi Lampinen, Sakari Tamminen, and Antti Oulasvirta. 2009. All My People Right Here, Right Now: management of group
co-presence on a social networking site. In Proceedings of the 2009 ACM International Conference on Supporting Group Work
(Sanibel Island, Florida, USA) (GROUP ’09). Association for Computing Machinery, New York, NY, USA, 281–290. doi:10.1145/
1531674.1531717
[48] Teddy Lazebnik, Lior Zalmanson, and Osnat Mokryn. 2025. Mind Your Manners: The Dynamics of Politeness in Human-AI vs.
Human-Human Interactions. Proc. ACM Hum.-Comput. Interact. 9, 7, Article CSCW450 (Oct. 2025), 22 pages. doi:10.1145/3757631
[49] Jingyu Lee and Youngki Lee. 2026. Probing Ambient Co-Presence as Social Infrastructure: First Encounters with Connected
Rooms. In Proceedings of the 2026 ACM Sustainability Week (ACM Sustainability Week ’26). Association for Computing Machinery,
New York, NY, USA, 477–484. doi:10.1145/3765611.3815495
[50] Grischa Liebel, Noah Langlois, and Kiev Gama. 2024. Challenges, Strengths, and Strategies of Software Engineers with ADHD: A
Case Study. In Proceedings of the 46th International Conference on Software Engineering: Software Engineering in Society (Lisbon,
Portugal) (ICSE-SEIS’24). Association for Computing Machinery, New York, NY, USA, 57–68. doi:10.1145/3639475.3640107
[51] Lu Liu, Harm van Essen, and Berry Eggen. 2025. What’s Happening in the Office: Designing Information Displays for Human-Like
Experience to Promote Workspace Awareness in Hybrid Work. Proc. ACM Hum.-Comput. Interact. 9, 7, Article CSCW523 (Oct.
2025), 29 pages. doi:10.1145/3757704
[52] Yuhan Luo, Bongshin Lee, Donghee Yvette Wohn, Amanda L. Rebar, David E. Conroy, and Eun Kyoung Choe. 2018. Time for
Break: Understanding Information Workers’ Sedentary Behavior Through a Break Prompting System. In Proceedings of the 2018
CHI Conference on Human Factors in Computing Systems (Montreal QC, Canada) (CHI ’18). Association for Computing Machinery,
New York, NY, USA, 1–14. doi:10.1145/3173574.3173701
[53] Wenhan Lyu, Yimeng Wang, Yifan Sun, and Yixuan Zhang. 2025. Will Your Next Pair Programming Partner Be Human? An
Empirical Evaluation of Generative AI as a Collaborative Teammate in a Semester-Long Classroom Setting. In Proceedings of the
Twelfth ACM Conference on Learning @ Scale (Palermo, Italy) (L@S ’25). Association for Computing Machinery, New York, NY,
USA, 83–94. doi:10.1145/3698205.3729544
[54] Qianou Ma, Tongshuang Wu, and Kenneth Koedinger. 2023. Is AI the better programming partner? Human-Human Pair
Programming vs. Human-AI pAIr Programming. (2023). arXiv:2306.05153 [cs.HC] https://arxiv.org/abs/2306.05153
[55] Aparajita S Marathe and Anne Marie Piper. 2025. The Accessibility Paradox: How Blind and Low Vision Employees Experience
and Negotiate Accessibility in the Technology Industry. Proc. ACM Hum.-Comput. Interact. 9, 7, Article CSCW485 (Oct. 2025),
25 pages. doi:10.1145/3757666
[56] André N. Meyer and Thomas Fritz. 2025. Better Balancing Focused Work and Collaboration in Hybrid Teams by Cultivating the
Sharing of Work Schedules. Proc. ACM Hum.-Comput. Interact. 9, 2, Article CSCW036 (May 2025), 28 pages. doi:10.1145/3710934

26

Pimenova et al.

[57] Courtney Miller, Paige Rodeghero, Margaret-Anne Storey, Denae Ford, and Thomas Zimmermann. 2021. "How Was Your
Weekend?" Software Development Teams Working From Home During COVID-19. In 2021 IEEE/ACM 43rd International Conference
on Software Engineering (ICSE). 624–636. doi:10.1109/ICSE43902.2021.00064
[58] Kevin Murphy and Russell A. Barkley. 1996. Attention deficit hyperactivity disorder adults: comorbidities and adaptive
impairments. Comprehensive Psychiatry 37, 6 (1996), 393–401. doi:10.1016/s0010-440x(96)90022-x
[59] Emerson Murphy-Hill, Ciera Jaspan, Caitlin Sadowski, David Shepherd, Michael Phillips, Collin Winter, Andrea Knight, Edward
Smith, and Matthew Jorde. 2021. What Predicts Software Developers’ Productivity? . IEEE Transactions on Software Engineering
47, 03 (March 2021), 582–594. doi:10.1109/TSE.2019.2900308
[60] Sebastian C. Müller and Thomas Fritz. 2015. Stuck and Frustrated or in Flow and Happy: Sensing Developers’ Emotions and
Progress. In 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering, Vol. 1. 688–699. doi:10.1109/ICSE.2015.334
[61] Kathleen G. Nadeau. 2005. Career choices and workplace challenges for individuals with ADHD. Journal of Clinical Psychology
61, 5 (2005), 549–563. https://pubmed.ncbi.nlm.nih.gov/15723424/
[62] Kaia Newman, Sarah Snay, Madeline Endres, Manasvi Parikh, and Andrew Begel. 2025. Disclosure of Neurodivergence in
Software Workplaces: a Mixed Methods Study of Forum and Survey Perspectives. In Proceedings of the 27th International ACM
SIGACCESS Conference on Computers and Accessibility (ASSETS ’25). Association for Computing Machinery, New York, NY, USA,
Article 82, 17 pages. doi:10.1145/3663547.3746334
[63] Kaia Newman, Sarah Snay, Madeline Endres, Manasvi Parikh, and Andrew Begel. 2025. "Get Me In The Groove": A Mixed
Methods Study on Supporting ADHD Professional Programmers. In Proceedings of the IEEE/ACM 47th International Conference on
Software Engineering (ICSE ’25). IEEE/ACM, 1217–1229. doi:10.1109/ICSE55347.2025.00242
[64] B. A. Oroian, P. Nechita, and A. Szalontay. 2024. Hyperfocus in ADHD: A Misunderstood Cognitive Phenomenon. Medical-Surgical
Journal (Revista Medico-Chirurgicala) 128, 1 (2024), 5–11. doi:10.1192/j.eurpsy.2025.662
[65] Aadarsh Padiyath and Tamara Nelson-Fromm. 2026. Reflecting on Thematic Analysis in Computer Science Education Research:
A Field Guide for Researchers and Reviewers. In Proceedings of the 57th ACM Technical Symposium on Computer Science Education
V.1 (USA) (SIGCSE TS 2026). Association for Computing Machinery, New York, NY, USA, 790–796. doi:10.1145/3770762.3772512
[66] Veronica Pimenova, Sarah Fakhoury, Christian Bird, Margaret-Anne Storey, and Madeline Endres. 2026. Good Vibrations?
A Qualitative Study of Co-Creation, Communication, Flow, and Trust in Vibe Coding. (2026). arXiv:2509.12491 [cs.SE]
https://arxiv.org/abs/2509.12491
[67] Veronica Pimenova, Yotam Sechayk, Fabricio Murai, Andrew Hundt, and Shiri Dori-Hacohen. 2025. A Longitudinal Autoethnography of Email Access for a Professional with Chronic Illness and ADHD: Preliminary Insights. In Proceedings of the 27th
International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS ’25). Association for Computing Machinery,
New York, NY, USA, Article 115, 4 pages. doi:10.1145/3663547.3759764
[68] Saima Ritonummi, Valtteri Siitonen, Markus Salo, Henri Pirkkalainen, and Anu Sivunen. 2023. Flow Experience in Software
Engineering. In Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of
Software Engineering (San Francisco, CA, USA) (ESEC/FSE 2023). Association for Computing Machinery, New York, NY, USA,
618–630. doi:10.1145/3611643.3616263
[69] Rafael A. Rivas-Vazquez, Samantha G. Diaz, Melina M. Visser, and Ana A. Rivas-Vazquez. 2023. Adult ADHD: Underdiagnosis of
a Treatable Condition. Journal of Health Service Psychology 49, 1 (Jan 2023), 11–19. doi:10.1007/s42843-023-00077-w
[70] Advait Sarkar and Ian Drosos. 2025. Vibe coding: programming through conversation with artificial intelligence. (2025).
arXiv:2506.23253 [cs.HC] https://arxiv.org/abs/2506.23253
[71] Prisilla Amiel Sarto, Erin Reese Lorzano, Alycia Artes, Helaena Marie Bobis, Grace Lorraine Intal, Donn Enrique Moreno, and
Maria Elaine Tan. 2026. A Strategic Approach to Developing AbiliNet: Leveraging the Business Model Canvas for an Inclusive
AI-Driven Job-Matching Platform. In Proceedings of the 9th International Conference on Business and Information Management
(ICBIM ’25). Association for Computing Machinery, New York, NY, USA, 28–35. doi:10.1145/3785171.3785188

Two’s a Crowd: Human and AI-Based Copresence for Developers with ADHD

27

[72] Ralph Schroeder. 2002. Copresence and Interaction in Virtual Environments: An Overview of the Range of Issues. In Proceedings
of the 5th International Workshop on Presence. Porto, Portugal, 274–295.
[73] Ralph Schroeder. 2006. Being There Together and the Future of Connected Presence. Presence: Teleoperators and Virtual
Environments 15, 4 (August 2006), 438–454. doi:10.1162/pres.15.4.438
[74] J. A. Sedgwick, A. Merwood, and P. Asherson. 2019. The positive aspects of attention deficit hyperactivity disorder: a qualitative
investigation of successful adults with ADHD. Attention Deficit and Hyperactivity Disorders 11, 3 (Sep 2019), 241–253. doi:10.
1007/s12402-018-0277-6
[75] Gina Sgro, Margaret Coit, Brianna D. Sullivan, Malia Valentine, Sammie Chavez, and Amanda Tran. 2025. Barriers to AttentionDeficit/Hyperactivity Disorder Diagnosis in Adults. Report. Office of the Assistant Secretary for Planning and Evaluation (ASPE).
https://aspe.hhs.gov/reports/barriers-adhd-diagnosis-adults
[76] Tom Shakespeare. 2006. The social model of disability. In The disability studies reader. Routledge, 16–24.
[77] Richard Skarbez, Frederick P. Brooks, Jr., and Mary C. Whitton. 2017. A Survey of Presence and Related Concepts. ACM Comput.
Surv. 50, 6, Article 96 (Nov. 2017), 39 pages. doi:10.1145/3134301
[78] Diomidis Spinellis. 2024. Pair programming with generative AI. IEEE Software 41, 3 (2024), 16–18.
[79] Philipp Spitzer, Joshua Holstein, Patrick Hemmer, Michael Vössing, Niklas Kühl, Dominik Martin, and Gerhard Satzger. 2025.
Human Delegation Behavior in Human-AI Collaboration: The Effect of Contextual Information. Proc. ACM Hum.-Comput.
Interact. 9, 2, Article CSCW101 (May 2025), 28 pages. doi:10.1145/3710999
[80] Stack Overflow. 2022. 2022 Developer Survey. Stack Overflow. https://survey.stackoverflow.co/2022/
[81] Marije Stolte, Victoria Trindade-Pons, Priscilla Vlaming, Babette Jakobi, Barbara Franke, Evelyn H. Kroesbergen, Matthijs
Baas, and Martine Hoogman. 2022. Characterizing Creative Thinking and Creative Achievements in Relation to Symptoms of
Attention-Deficit/Hyperactivity Disorder and Autism Spectrum Disorder. Frontiers in Psychiatry 13 (2022), 909202. doi:10.3389/
fpsyt.2022.909202
[82] Margaret-Anne Storey. 2026. From Technical Debt to Cognitive and Intent Debt: Rethinking Software Health in the Age of AI.
(2026). arXiv:2603.22106 [cs.SE] https://arxiv.org/abs/2603.22106
[83] Niran Subramaniam, Joe Nandhakumar, and João Baptista. 2013. Exploring social network interactions in enterprise systems: the
role of virtual co-presence. Information Systems Journal 23, 6 (2013), 475–499. doi:10.1111/isj.12019
[84] Josh Tenenberg, Wolff-Michael Roth, and David Socha. 2016. From I-Awareness to We-Awareness in CSCW. Comput. Supported
Coop. Work 25, 4–5 (Oct. 2016), 235–278. doi:10.1007/s10606-014-9215-0
[85] Kosuke Teruyama, Fuko Hisada, Jacqueline Urakami, Masahiro Inagaki, Ryuta Harima, Tomoko Hachiya, Naoyuki Tamai, and
Tomohiro Ogawa. 2025. The Vision Pit: Enhancing Remote Collaboration through Simulated Spatial Co-presence. In Proceedings
of the Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA ’25). Association for Computing
Machinery, New York, NY, USA, Article 527, 9 pages. doi:10.1145/3706599.3719840
[86] Tam Nguyen Thanh, Michael Morgan, Matthew Butler, and Kim Marriott. 2019. Perfect Match: Facilitating Study Partner
Matching. In Proceedings of the 50th ACM Technical Symposium on Computer Science Education (Minneapolis, MN, USA) (SIGCSE
’19). Association for Computing Machinery, New York, NY, USA, 1102–1108. doi:10.1145/3287324.3287344
[87] Christoph Treude and Margaret-Anne Storey. 2025. Generative AI and empirical software engineering: A paradigm shift. In 2025
2nd IEEE/ACM International Conference on AI-powered Software (AIware). IEEE, 233–239.
[88] Yael Turjeman-Levi, Guy Itzchakov, and Batya Engel-Yeger. 2024. Executive function deficits mediate the relationship between
employees’ ADHD and job burnout. AIMS Public Health 11, 1 (Mar 2024), 294–314. doi:10.3934/publichealth.2024015 PMID:
38617412.
[89] Pragya Verma, Marcos Vinicius Cruz, and Grischa Liebel. 2025. Differences between neurodivergent and neurotypical software
engineers: Analyzing the 2022 stack overflow survey. In Euromicro Conference on Software Engineering and Advanced Applications.
Springer, 57–74. doi:10.1007/978-3-032-04207-1_5

28

Pimenova et al.

[90] Nadav Viduchinsky. 2026. The Algorithmic Mirror: Knowledge Creation and Self-Perception in Dating Applications. In Proceedings
of the 2026 CHI Conference on Human Factors in Computing Systems (CHI ’26). Association for Computing Machinery, New York,
NY, USA, Article 108, 13 pages. doi:10.1145/3772318.3790901
[91] Emily Q. Wang and Anne Marie Piper. 2022. The Invisible Labor of Access in Academic Writing Practices: A Case Analysis with
Dyslexic Adults. Proceedings of the ACM on Human-Computer Interaction 6, CSCW1, Article 120 (2022), 25 pages. doi:10.1145/
3512967
[92] Holly A. White and Priti Shah. 2011. Creative style and achievement in adults with attention-deficit/hyperactivity disorder.
Personality and Individual Differences 50, 5 (2011), 673–677. doi:10.1016/j.paid.2010.12.015
[93] Laurie Williams, Robert R Kessler, Ward Cunningham, and Ron Jeffries. 2000. Strengthening the case for pair programming.
IEEE software 17, 4 (2000), 19–25. doi:10.1109/52.854064
[94] Shaomei Wu, Jingjin Li, and Gilly Leshed. 2024. Finding My Voice over Zoom: An Autoethnography of Videoconferencing
Experience for a Person Who Stutters. In Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems (Honolulu,
HI, USA) (CHI ’24). Association for Computing Machinery, New York, NY, USA, Article 916, 16 pages. doi:10.1145/3613904.3642746
[95] Takanobu Yamamoto. 2022. The relationship between central fatigue and attention deficit/hyperactivity disorder of the inattentive
type. Neurochemical research 47, 9 (2022), 2890–2898. doi:10.1007/s11064-022-03693-y
[96] Shuning Zhang, Hui Wang, and Xin Yi. 2025. Exploring Collaboration Patterns and Strategies in Human-AI Co-creation through
the Lens of Agency: A Scoping Review of the Top-tier HCI Literature. Proc. ACM Hum.-Comput. Interact. 9, 7, Article CSCW413
(Oct. 2025), 43 pages. doi:10.1145/3757594
[97] Shanyang Zhao. 2003. Toward a Taxonomy of Copresence. Presence: Teleoperators and Virtual Environments 12, 5 (October 2003),
445–455. doi:10.1162/105474603322761261
[98] Xiyu Zhou, Peng Liang, Beiqi Zhang, Zengyang Li, Aakash Ahmad, Mojtaba Shahin, and Muhammad Waseem. 2025. Exploring
the problems, their causes and solutions of AI pair programming: A study on GitHub and Stack Overflow. 17 pages. doi:10.1016/
j.jss.2024.112204
[99] Zoom Communications Inc. [n. d.]. Meet My Notes: Your new AI note taker. https://www.zoom.com/en/products/ai-assistant/
features/ai-note-taking
```
