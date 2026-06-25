import { mkdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = new URL('../assets/social-cards/', import.meta.url);
mkdirSync(outDir, { recursive: true });

const cards = [
  {
    file: 'week01-foundation.svg',
    label: 'WEEK 1 RECAP',
    title: 'Trust Foundation',
    subtitle: 'Before growth, build something real to point to.',
    blocks: ['SEO', 'Search Console', 'Blog', 'X', 'Discord', 'LinkedIn', 'GitHub'],
    footer: 'SandBase.ai — 30-day AI infra growth journal',
  },
  {
    file: 'day01-seo-crawlability.svg',
    label: 'DAY 1',
    title: 'Can Google See the Site?',
    subtitle: 'Before content, fix crawlability.',
    blocks: ['Browser 200', 'Googlebot 404', 'Find root cause', 'Fix crawler fallback'],
    footer: 'SEO starts with crawlability, not keywords.',
  },
  {
    file: 'day02-verification.svg',
    label: 'DAY 2',
    title: 'Verification Is Growth Work',
    subtitle: 'Do not ask Google to index a broken page.',
    blocks: ['Googlebot 200', 'Canonical host', 'Sitemap OK', 'Search Console ready'],
    footer: 'A fix is done only after crawler-side verification.',
  },
  {
    file: 'day03-x-build-signal.svg',
    label: 'DAY 3',
    title: 'X as a Build Signal',
    subtitle: 'One clear post beats link spam.',
    blocks: ['Logo', 'Bio', 'Website', 'First post', 'Daily build note'],
    footer: 'New accounts should look real before chasing reach.',
  },
  {
    file: 'day04-discord-community.svg',
    label: 'DAY 4',
    title: 'Discord as Product Infrastructure',
    subtitle: 'Small and clear beats big and empty.',
    blocks: ['Start here', 'Quickstart', 'Ask for help', 'Report bugs'],
    footer: 'A community should help builders know where to go.',
  },
  {
    file: 'day05-linkedin-trust.svg',
    label: 'DAY 5',
    title: 'LinkedIn Builds B2B Trust',
    subtitle: 'A company page is a credibility object.',
    blocks: ['Company page', 'About', 'Website', 'First post', 'Company author'],
    footer: 'B2B trust starts with a public company identity.',
  },
  {
    file: 'day06-blog-system.svg',
    label: 'DAY 6',
    title: 'Blog as Content Infrastructure',
    subtitle: 'The website explains the product. The blog explains the category.',
    blocks: ['Markdown', 'RSS', 'Sitemap', 'JSON-LD', 'Topic clusters'],
    footer: 'Technical content compounds when it has a system.',
  },
  {
    file: 'day07-trust-system.svg',
    label: 'DAY 7',
    title: 'Connect the Trust System',
    subtitle: 'Website + Blog + GitHub + Community tell one story.',
    blocks: ['Website', 'Blog clusters', 'GitHub repo', 'Discord feedback', 'LinkedIn', 'X'],
    footer: 'Week 2 distribution needs a real foundation to point to.',
  },
  {
    file: 'day08-distribution.svg',
    label: 'DAY 8',
    title: 'Distribution After Trust',
    subtitle: 'Fewer, better placements beat link dumping.',
    blocks: ['Dev.to', 'Directories', 'GitHub', 'Communities', 'LinkedIn', 'X'],
    footer: 'Distribution works better after trust exists.',
  },
  {
    file: 'agent-sandbox-runtime-checklist.svg',
    label: 'RUNTIME CHECKLIST',
    title: 'Agent Sandbox Runtime Checklist',
    subtitle: 'Before, during, and after execution.',
    blocks: ['Capabilities', 'Filesystem', 'Network', 'Lifecycle', 'Audit', 'Integration'],
    footer: 'Production agents need runtime boundaries operators can inspect.',
  },
];

function esc(value) {
  return value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
}

function blockSvg(text, x, y, w = 190) {
  return `
    <g>
      <rect x="${x}" y="${y}" width="${w}" height="72" rx="14" fill="#f8faf9" stroke="#d7dfdc"/>
      <circle cx="${x + 28}" cy="${y + 36}" r="8" fill="#14b89a"/>
      <text x="${x + 48}" y="${y + 42}" font-family="Inter, Arial, sans-serif" font-size="22" font-weight="650" fill="#111318">${esc(text)}</text>
    </g>`;
}

function cardSvg(card) {
  const cols = card.blocks.length <= 4 ? 2 : card.blocks.length <= 6 ? 3 : 4;
  const w = cols === 2 ? 420 : cols === 3 ? 310 : 230;
  const startX = cols === 2 ? 340 : cols === 3 ? 225 : 135;
  const rowGap = 104;
  const blocks = card.blocks.map((b, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    return blockSvg(b, startX + col * (w + 24), 440 + row * rowGap, w);
  }).join('\n');

  return `<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-label="${esc(card.title)}">
  <rect width="1600" height="900" fill="#f3f1ea"/>
  <path d="M0 0h1600v900H0z" fill="#f3f1ea"/>
  <g opacity="0.42" stroke="#d8dedb" stroke-width="1">
    ${Array.from({ length: 17 }, (_, i) => `<path d="M${i * 100} 0v900"/>`).join('')}
    ${Array.from({ length: 10 }, (_, i) => `<path d="M0 ${i * 100}h1600"/>`).join('')}
  </g>
  <circle cx="1340" cy="130" r="210" fill="#d8e8e4" opacity="0.72"/>
  <circle cx="260" cy="760" r="170" fill="#e2e0d7" opacity="0.75"/>

  <rect x="96" y="72" width="1408" height="756" rx="32" fill="#fffdf8" stroke="#d6d1c4" stroke-width="2"/>
  <rect x="132" y="112" width="230" height="44" rx="22" fill="#111318"/>
  <text x="156" y="141" font-family="Inter, Arial, sans-serif" font-size="20" font-weight="800" letter-spacing="2" fill="#ffffff">${esc(card.label)}</text>

  <text x="132" y="255" font-family="Inter, Arial, sans-serif" font-size="74" font-weight="850" fill="#111318">${esc(card.title)}</text>
  <text x="136" y="322" font-family="Inter, Arial, sans-serif" font-size="32" font-weight="500" fill="#4e5552">${esc(card.subtitle)}</text>

  <g>
    <rect x="132" y="374" width="1336" height="2" fill="#dce2df"/>
    <circle cx="132" cy="375" r="7" fill="#14b89a"/>
    <circle cx="1468" cy="375" r="7" fill="#14b89a"/>
  </g>

  ${blocks}

  <text x="132" y="780" font-family="Inter, Arial, sans-serif" font-size="24" font-weight="600" fill="#111318">${esc(card.footer)}</text>
  <text x="132" y="812" font-family="Inter, Arial, sans-serif" font-size="18" fill="#6b716e">github.com/sandbaseai/zero-to-one-ai-infra-growth</text>
</svg>`;
}

for (const card of cards) {
  writeFileSync(join(outDir.pathname, card.file), cardSvg(card), 'utf8');
}

console.log(`Generated ${cards.length} social cards in ${outDir.pathname}`);
