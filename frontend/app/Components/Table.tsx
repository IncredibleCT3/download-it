"use client"

import { useState } from "react";

interface GameData {
  id: number;
  title: string;
  channel: string;
  players: string;
  rating: number;
}

const gameData: GameData[] = [
  { id: 1, title: "Wii Sports", channel: "Disc Channel", players: "1-4", rating: 5 },
  { id: 2, title: "Mario Kart Wii", channel: "Disc Channel", players: "1-4", rating: 5 },
  { id: 3, title: "Wii Fit", channel: "Disc Channel", players: "1", rating: 4 },
  { id: 4, title: "Super Smash Bros. Brawl", channel: "Disc Channel", players: "1-4", rating: 5 },
  { id: 5, title: "The Legend of Zelda: Twilight Princess", channel: "Disc Channel", players: "1", rating: 5 },
  { id: 6, title: "Wii Play", channel: "Disc Channel", players: "1-2", rating: 4 },
  { id: 7, title: "New Super Mario Bros. Wii", channel: "Disc Channel", players: "1-4", rating: 5 },
];

export function Table() {
  const [selectedRow, setSelectedRow] = useState<number | null>(null);
  const [hoveredRow, setHoveredRow] = useState<number | null>(null);

  return (
    <div className="w-full max-w-5xl">
      <div className="minimal-container">
        {/* Table Container */}
        <div className="minimal-table-wrapper">
          <table className="minimal-table">
            <thead>
              <tr>
                <th className="minimal-th">Title</th>
                <th className="minimal-th">Author</th>
                <th className="minimal-th">Duration</th>
                <th className="minimal-th">Folder</th>
              </tr>
            </thead>
            <tbody>
              {gameData.map((game) => (
                <tr
                  key={game.id}
                  className={`minimal-tr ${
                    selectedRow === game.id ? "minimal-tr-selected" : ""
                  } ${hoveredRow === game.id ? "minimal-tr-hover" : ""}`}
                  onClick={() => setSelectedRow(game.id)}
                  onMouseEnter={() => setHoveredRow(game.id)}
                  onMouseLeave={() => setHoveredRow(null)}
                >
                  <td className="minimal-td">{game.title}</td>
                  <td className="minimal-td">{game.channel}</td>
                  <td className="minimal-td">{game.players}</td>
                  <td className="minimal-td">
                    <div className="flex gap-1">
                      {[...Array(5)].map((_, i) => (
                        <span
                          key={i}
                          className={`minimal-star ${
                            i < game.rating ? "minimal-star-filled" : ""
                          }`}
                        >
                          ★
                        </span>
                      ))}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      <style>{`
        .minimal-container {
          background: #0a0a0a;
          border-radius: 0;
          padding: 0;
        }

        .minimal-header {
          text-align: center;
          margin-bottom: 48px;
        }

        .minimal-header h1 {
          color: #ffffff;
          font-size: 32px;
          font-weight: 700;
          letter-spacing: -0.5px;
        }

        .minimal-table-wrapper {
          background: transparent;
          border-radius: 0;
          padding: 0;
        }

        .minimal-table {
          width: 100%;
          border-collapse: collapse;
        }

        .minimal-th {
          padding: 16px 20px;
          text-align: left;
          color: #666666;
          font-weight: 500;
          background: transparent;
          border-bottom: 1px solid #1a1a1a;
          font-size: 14px;
          text-transform: uppercase;
          letter-spacing: 0.5px;
        }

        .minimal-tr {
          cursor: pointer;
          transition: all 0.15s ease;
        }

        .minimal-td {
          padding: 20px;
          background: #0f0f0f;
          border-bottom: 1px solid #1a1a1a;
          transition: all 0.15s ease;
          color: #e5e5e5;
          font-size: 15px;
        }

        .minimal-tr:first-child .minimal-td {
          border-top: 1px solid #1a1a1a;
        }

        .minimal-tr-hover .minimal-td {
          background: #1a1a1a;
        }

        .minimal-tr-selected .minimal-td {
          background: #2a2a2a;
          border-bottom-color: #333333;
          color: #ffffff;
        }

        .minimal-tr-selected:first-child .minimal-td {
          border-top-color: #333333;
        }

        .minimal-star {
          font-size: 16px;
          color: #2a2a2a;
          transition: all 0.2s ease;
        }

        .minimal-star-filled {
          color: #ffffff;
        }

        .minimal-tr-selected .minimal-star-filled {
          color: #ffffff;
        }
      `}</style>
    </div>
  );
}

export default Table